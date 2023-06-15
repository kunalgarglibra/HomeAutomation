<a name="br1"></a> 

**Project**

**Presentation**

SEP 769: Cyber

Physical Systems

Home Automation System using

Raspberry Pi

Group 6:

**Deeya Tangri**

(400425055)

**Kunal Garg**

(400387739)

mcmaster.ca



<a name="br2"></a> 

**Overview**

**Home Automation System: The Future of Smart Living**

• Automatically control Fan and Light in our homes based on Room Temperature and Light

Intensity using a Raspberry Pi.

• Components Involved: Raspberry Pi, Temperature-Humidity Sensor (DHT11), Light Intensity

Sensor (GY-30), Actuator (Stepper Motor – Fan), LED.

• Communication: Raspberry Pi sends the sensor data to ThingsBoard Cloud Platform where

the data is visualized as Dashboards for monitoring purposes, analysis, and decision-

making.

• Raspberry Pi determines optimal settings based on predefined thresholds and accordingly

controls the Actuator and the LED.

mcmaster.ca

15 June 2023

|

2



<a name="br3"></a> 

Raspberry Pi

Stepper Motor

Driver

Stepper

Motor

**Home**

**Automation**

**System**

LED

External

Power

Supply

Temperature

Humidity

Sensor

Light Intensity

Sensor

mcmaster.ca

15 June 2023

|

3



<a name="br4"></a> 

**Hardware Requirements**

**DHT11 Sensor**

**GY-30 Sensor**

**Stepper Motor &**

**ULN2003 Driver**

**Breadboard**

**LED**

**Raspberry Pi**

**SparkFun 40-Pin**

**Wedge Connector**

**1K Ohm Resistor**

**Power Supply**

**Module & Battery**

**Jumper Wires**

mcmaster.ca

15 June 2023

|

4



<a name="br5"></a> 

**Software Requirements**

**ThingsBoard IOT Cloud Platform**

**Raspberry PI OS**

mcmaster.ca

15 June 2023

|

5



<a name="br6"></a> 

**Hardware Setup**

**(Circuit Schematic Diagram)**

mcmaster.ca

15 June 2023

|

6



<a name="br7"></a> 

Pin Configuration

Connections

Vcc

Part

Rpi Pins

3\.3V Pin

GPIO 13

GND Pin

3\.3V Pin

SCL Pin

SDA Pin

3\.3V Pin

GND Pin

GPIO 17

GND Pin

GPIO 18

GPIO 23

GPIO 24

GPIO 25

Neg Pin of HW 131

Pos Pin of HW 131

B

DHT 11

Data

Ground

Vcc

Scl

GY-30

Led

Sda

Ado

Ground

**Pin**

**Connections**

Anode(Longer Leg)

Cathode(Smaller Leg)

Input 1

Input 2

Input 3

ULN2003 Stepper Motor Driver

Input 4

Negative Pin(Ext PS)

Positive Pin(Ext PS)

Coil 2(Pink)

Coil 4(Blue)

5 V(Red)

A

Stepper Motor

Coil 3(Yellow)

Coil 1(Orange)

C

D

mcmaster.ca

15 June 2023

|

7



<a name="br8"></a> 

**System Operation Flowchart**

mcmaster.ca

15 June 2023

|

8



<a name="br9"></a> 

**ThingsBoard Cloud Analysis**

Dashboards created on the ThingsBoard Cloud Platform:

mcmaster.ca

15 June 2023

|

9



<a name="br10"></a> 

**Temperature Dashboard:**

mcmaster.ca

15 June 2023 | 10



<a name="br11"></a> 

**Light Intensity Dashboard:**

mcmaster.ca

15 June 2023

|

11



<a name="br12"></a> 

**Humidity Dashboard:**

mcmaster.ca

15 June 2023 | 12



<a name="br13"></a> 

**Future Scope**

Additional control of LED and Fan with the help of a mobile/ web application

Other actuators similar to the stepper motor can be used for opening and closing of

windows, doors, etc with the help of desired sensors

This system can serve excellent purpose for monitoring the room of a newly born child

Automated system for thermostat control in the house

Intimating home-owners via personalised notification system whenever house controls

are changed/ hindered with

mcmaster.ca

15 June 2023 | 13



<a name="br14"></a> 

**References**

• <https://how2electronics.com/smart-phone-controlled-home-automation-with-raspberry-pi/>

• <https://thingsboard.cloud/dashboards/all/c84e1730-0962-11ee-b864-d528757047e3>

• [https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-](https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/)

[l293d-uln2003a/](https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/)

• <http://wiki.sunfounder.cc/index.php?title=GY-30_Digital_Light_Intensity_Measuring_Module>

mcmaster.ca

15 June 2023 | 14



<a name="br15"></a> 

Thank You!

J

