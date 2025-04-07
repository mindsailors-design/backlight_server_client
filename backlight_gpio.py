from gpiozero import PWMLED
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

factory = LGPIOFactory()
led1 = PWMLED(12, pin_factory=factory)
led2 = PWMLED(13, pin_factory=factory)
led1.value = 0
led2.value = 0

step = 0.1
delay = 0.5

for i in range(11):
    value = i * step
    led1.value = value
    led2.value = value
    print(f"Set PWM to {value:.1f}")
    sleep(delay)
led1.value = 0
led2.value = 0

# # led1.blink(on_time=2, off_time=2)
# while True:
#     # led2.toggle()
#     led1.value = 0
#     led2.value = 1
#     sleep(2)
#     led1.value = 1
#     led2.value = 0
#     sleep(2)