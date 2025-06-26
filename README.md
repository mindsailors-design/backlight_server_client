# Description
This repo is a simple python project for controlling led backlight on a e-paper display from a Kobo Clara HD.

## Server "backlight_server.py" 
This is a simple Rest API. It uses uvicorn as an async server and FastAPI as a Python framework.
There are endpoints for controlling brightness and color temperature using PWM on GPIO.

## Client "backlight_gpio.py"
Simple client made with typer framework as a TUI for interacting with server for controlling e-paper screen's backlight.
It uses HTTP requests to interact with server's RestAPI.
You can set, get, increase, decrease backlight's brightness and color temperature.

## GPIO test "backlight_gpio.py"
This is only a simple script to test hardware (GPIO, PWM, leds) without servers, clients, etc.

## Systemd service "backlight-api.client"
