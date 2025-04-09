from contextlib import asynccontextmanager
from fastapi import FastAPI
from gpiozero import PWMLED
from gpiozero.pins.lgpio import LGPIOFactory

WARM_LED = 12
COOL_LED = 13

brightness = 0.1
color_temp = 0.1

factory = None
warm_led = None
cool_led = None

def clamp(value):
    return max(0.0, min(1.0, value))

def set_pwm():
    print("Setting PWM")
    warm_led.value = brightness * (1.0 - color_temp)
    print("warm led: ", warm_led.value)
    cool_led.value = brightness * color_temp
    print("cool led: ", cool_led.value)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("GPIO Setup, running only once")
    global factory, warm_led, cool_led
    factory = LGPIOFactory()
    warm_led = PWMLED(WARM_LED, pin_factory=factory)
    cool_led = PWMLED(COOL_LED, pin_factory=factory)
    set_pwm()
    yield
    print("GPIO cleanup, running only once on shutdown")
    warm_led.close()
    cool_led.close()

app = FastAPI(lifespan=lifespan)

@app.post("/set_brightness")
def set_brightness(data: float):
    global brightness
    brightness = clamp(data)
    print(f"set_brightness: {brightness}")
    set_pwm()

    return brightness

@app.post("/increase_brightness")
def increase_brightness():
    global brightness
    brightness = clamp(brightness + 0.1)
    print(f"increase_brightness: {brightness}")
    set_pwm()

    return brightness

@app.post("/decrease_brightness")
def decrease_brightness():
    global brightness
    brightness = clamp(brightness - 0.1)
    print(f"decrease_brightness: {brightness}")
    set_pwm()

    return brightness

@app.post("/set_color_temp")
def set_color_temp(data: float):
    global color_temp
    color_temp = clamp(data)
    print(f"set_color_temp: {color_temp}")
    set_pwm()

    return color_temp

@app.post("/increase_color_temp")
def increase_color_temp():
    global color_temp
    color_temp = clamp(color_temp + 0.1)
    print(f"increase_color_temp: {color_temp}")
    set_pwm()

    return color_temp

@app.post("/decrease_color_temp")
def decrease_color_temp():
    global color_temp
    color_temp = clamp(color_temp - 0.1)
    print(f"decrease_color_temp: {color_temp}")
    set_pwm()

    return color_temp

@app.get("/get_brightness")
def get_brightness():
    global brightness
    print(f"get_brightness: {brightness}")

    return brightness

@app.get("/get_color_temp")
def get_color_temp():
    global color_temp
    print(f"get_color_temp: {color_temp}")
    
    return color_temp