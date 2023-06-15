import Adafruit_DHT
import RPi.GPIO as GPIO
import os
import time

import sys
import board
import paho.mqtt.client as mqtt
import adafruit_dht
import json
import Adafruit_DHT
import smbus

ledPin = 17    # define ledPin

#motorPins = (12, 16, 18, 22)    # define pins connected to four phase ABCD of stepper motor
motorPins = (18,23,24,25) 
CCWStep = (0x01,0x02,0x04,0x08) # define power supply order for rotating anticlockwise 
CWStep = (0x08,0x04,0x02,0x01) 

sensor = Adafruit_DHT.DHT11
dht_pin = 13  # GPIO pin connected to the DHT11 sensor
threshold_temperature = 25

THINGSBOARD_HOST = 'thingsboard.cloud'
ACCESS_TOKEN = '6S99GNIa7pp3UX6ialaG'

sensor = Adafruit_DHT.DHT11
dht_pin = 13  

# Define some constants from the datasheet

DEVICE     = 0x5C # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on 
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
time.sleep(1)


GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
print ('using pin%d'%ledPin)

  
#GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
for pin in motorPins:
    GPIO.setup(pin,GPIO.OUT)

def destroy():
    GPIO.cleanup()                      # Release all GPIO

def LedOn():
    GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
    print ('led turned on >>>')     # print information on terminal
    
def LedOff():
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output HIGH level to turn on led
    print ('led turned off >>>')     # print information on terminal

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  # Read data from I2C interface
  #data = bus.read_i2c_block_data(0x04,0x02,4)
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)
                
# as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
def moveOnePeriod(direction,ms):    
    for j in range(0,4,1):      # cycle for power supply order
        for i in range(0,4,1):  # assign to each pin
            if (direction == 1):# power supply order clockwise
                GPIO.output(motorPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            else :              # power supply order anticlockwise
                GPIO.output(motorPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
            ms = 3
        time.sleep(ms*0.001)    
        
# continuous rotation function, the parameter steps specifies the rotation cycles, every four steps is a cycle
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
        
# function used to stop motor
def motorStop():
    for i in range(0,4,1):
        GPIO.output(motorPins[i],GPIO.LOW)

def StepStart():
    moveSteps(1,3,360)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
    time.sleep(1)
    moveSteps(0,3,360)  # rotating 360 deg anticlockwise
    time.sleep(1)
        
def StepStop():
    for i in range(0,4,1):
        GPIO.output(motorPins[i],False)
    

def destroy():
    GPIO.cleanup()             # Release resource
    
# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

# Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT11(board.D4)
#dhtDevice = 13

DHTsensor_data = {'temperature': 0, 'humidity': 0}
LDRsensor_data = {'Light Intensity': 0}

next_reading = time.time() 

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    print ('Stepper Program is starting...')
    print ('Led Program is starting ... \n')

    while True:
        lightLevel=readLight()
        #print("Light Level : " + format(lightLevel,'.2f') + " lx")
        time.sleep(0.5)
        LDRsensor_data['Light Intensity'] = format(lightLevel,'.2f')
        # Sending light intensity data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(LDRsensor_data), 1)
        
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        DHTsensor_data['temperature'] = temperature
        DHTsensor_data['humidity'] = humidity

        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(DHTsensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        
        if lightLevel is not None:
            print("Light Level : " + format(lightLevel,'.2f') + " lx")

            if lightLevel == 0:
                # Move the stepper motor clockwise with 200 steps
                LedOn()
                print("Light On")
                
            else:
                # Move the stepper motor counterclockwise with 200 steps
                LedOff()
                print("Light Off")

        if humidity is not None and temperature is not None:
            print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))

            if temperature > threshold_temperature:
                # Move the stepper motor clockwise with 200 steps
                print("Temperature Reached")
                StepStart()
            else:
                # Move the stepper motor counterclockwise with 200 steps
                StepStop()
                print("Temperature not reached")
                
                
        else:
            print("Failed to retrieve data from DHT11 sensor.")
        
        if sleep_time > 0:
            time.sleep(sleep_time)
            

except KeyboardInterrupt:
    destroy()
