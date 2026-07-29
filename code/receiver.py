# type: ignore
from machine import Pin, PWM, ADC
import time

sensor = ADC(26)

in1 = Pin(2, Pin.OUT)
in2 = Pin(3, Pin.OUT)

ena = PWM(Pin(4))
ena.freq(1000)

in1.value(1)
in2.value(0)

while True:
    light = sensor.read_u16()

    if light > 40000:
        speed = 25000     # Slow
    else:
        speed = 60000     # Normal

    ena.duty_u16(speed)

    print(light)

    time.sleep(0.05)
