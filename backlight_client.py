import typer
import requests

MAIN_URL = "http://127.0.0.1:8000"

SET_BRIGHTNESS_URL      = "/set_brightness"
SET_COLOR_TEMP_URL      = "/set_color_temp"
INCREASE_BRIGHTNESS_URL = "/increase_brightness"
DECREASE_BRIGHTNESS_URL = "/decrease_brightness"
INCREASE_COLOR_TEMP_URL = "/increase_color_temp"
DECREASE_COLOR_TEMP_URL = "/decrease_color_temp"
GET_BRIGHTNRESS_URL     = "/get_brightness"
GET_COLOR_TEMP_URL      = "/get_color_temp"

COMMON_HEADER = {"accept": "application/json"}

app = typer.Typer()

@app.command()
def set_brightness(brightness: float):
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/set_brightness?data=1' \
    -H 'accept: application/json' \
    -d ''
    """
    print(f"Setting brightness: {brightness}")

    url = MAIN_URL + SET_BRIGHTNESS_URL
    params = {"data": brightness}

    response = requests.post(url, headers=COMMON_HEADER, params=params)
    print(response.status_code)
    print(response.text)

@app.command()
def set_color_temp(color_temp: float):
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/set_color_temp?data=1' \
    -H 'accept: application/json' \
    -d ''
    """
    print(f"Setting color temperature: {color_temp}")

    url = MAIN_URL + SET_COLOR_TEMP_URL
    params = {"data": color_temp}

    response = requests.post(url, headers=COMMON_HEADER, params=params)
    print(response.status_code)
    print(response.text)

@app.command()
def increase_brightness():
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/increase_brightness' \
    -H 'accept: application/json' \
    -d ''
    """
    print("Increasing brightness")

    url = MAIN_URL + INCREASE_BRIGHTNESS_URL

    response = requests.post(url, headers=COMMON_HEADER)
    print(response.status_code)
    print(response.text)

@app.command()
def decrease_brightness():
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/decrease_brightness' \
    -H 'accept: application/json' \
    -d ''
    """
    print("Decreasing brightness")

    url = MAIN_URL + DECREASE_BRIGHTNESS_URL

    response = requests.post(url, headers=COMMON_HEADER)
    print(response.status_code)
    print(response.text)

@app.command()
def increase_color_temp():
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/increase_color_temp' \
    -H 'accept: application/json' \
    -d ''
    """
    print("Increasing color temperature")

    url = MAIN_URL + INCREASE_COLOR_TEMP_URL

    response = requests.post(url, headers=COMMON_HEADER)
    print(response.status_code)
    print(response.text)

@app.command()
def decrease_color_temp():
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/decrease_color_temp' \
    -H 'accept: application/json' \
    -d ''
    """
    print("Decreasing color temperature")

    url = MAIN_URL + DECREASE_COLOR_TEMP_URL

    response = requests.post(url, headers=COMMON_HEADER)
    print(response.status_code)
    print(response.text)

@app.command()
def get_brightness():
    """
    curl -X 'GET' \
    'http://127.0.0.1:8000/get_brightness' \
    -H 'accept: application/json'
    """
    print("Getting brightness")

    url = MAIN_URL + GET_BRIGHTNRESS_URL

    response = requests.get(url, headers=COMMON_HEADER)

    print(response.status_code)
    print(response.text)

@app.command()
def get_color_temp():
    """
    curl -X 'GET' \
    'http://127.0.0.1:8000/get_color_temp' \
    -H 'accept: application/json'
    """
    print("Getting color temperature")

    url = MAIN_URL + GET_COLOR_TEMP_URL

    response = requests.get(url, headers=COMMON_HEADER)

    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    app()