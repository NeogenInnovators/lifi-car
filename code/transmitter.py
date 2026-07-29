# type: ignore
from machine import Pin
import time

led = Pin(15, Pin.OUT)

while True:
    # Speed Limit Signal
    for i in range(200):
        led.on()
        time.sleep_us(500)
        led.off()
        time.sleep_us(500)

    time.sleep(1)
