from machine import Pin
from time import sleep
 
sensor = Pin(2, Pin.OUT)
 
while True:
 sensor.value(not sensor.value())
 sleep(1/2)


