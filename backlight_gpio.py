from gpiozero import PWMLED
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

factory = LGPIOFactory()
led1 = PWMLED(12, pin_factory=factory)
led2 = PWMLED(13, pin_factory=factory)
led1.value = 0
led2.value = 0


led1.blink(on_time=2, off_time=2)
while True:
    led2.toggle()
    sleep(1)