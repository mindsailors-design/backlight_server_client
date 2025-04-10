import typer
import requests

MAIN_URL = "http://127.0.0.1:8000"

app = typer.Typer()

@app.command()
def set_brightness(brightness: float):
    print(f"Setting brightness, {brightness}")
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/set_brightness?data=1' \
    -H 'accept: application/json' \
    -d ''
    """

    set_brightness_url = "/set_brightness"
    url = MAIN_URL + set_brightness_url
    params = {"data": brightness}
    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers, params=params, data="")
    print(response.status_code)
    print(response.text)

@app.command()
def set_color_temp(color_temp: float):
    print(f"Setting color temperature: {color_temp}")
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/set_color_temp?data=1' \
    -H 'accept: application/json' \
    -d ''
    """

    set_color_temp_url = "/set_color_temp"
    url = MAIN_URL + set_color_temp_url
    params = {"data": color_temp}
    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers, params=params, data = "")
    print(response.status_code)
    print(response.text)

@app.command()
def increase_brightness():
    print("Increasing brightness")
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/increase_brightness' \
    -H 'accept: application/json' \
    -d ''
    """

    increase_brightness_url = "/increase_brightness"
    url = MAIN_URL + increase_brightness_url

    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers)
    print(response.status_code)
    print(response.text)

@app.command()
def decrease_brightness():
    print("Decreasing brightness")
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/decrease_brightness' \
    -H 'accept: application/json' \
    -d ''
    """

    decrease_brightness_url = "/decrease_brightness"
    url = MAIN_URL + decrease_brightness_url

    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers)
    print(response.status_code)
    print(response.text)

@app.command()
def increase_color_temp():
    print("Increasing color temperature")
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/increase_color_temp' \
    -H 'accept: application/json' \
    -d ''
    """

    increase_color_temp_url = "/increase_color_temp"
    url = MAIN_URL + increase_color_temp_url

    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers)
    print(response.status_code)
    print(response.text)

@app.command()
def decrease_color_temp():
    print("Decreasing color temperature")
    """
    curl -X 'POST' \
    'http://127.0.0.1:8000/decrease_color_temp' \
    -H 'accept: application/json' \
    -d ''
    """

    decrease_color_temp_url = "/decrease_color_temp"
    url = MAIN_URL + decrease_color_temp_url

    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers)
    print(response.status_code)
    print(response.text)

@app.command()
def get_brightness():
    print("Getting brightness")

    """
    curl -X 'GET' \
    'http://127.0.0.1:8000/get_brightness' \
    -H 'accept: application/json'
    """

    get_brightness_url = "/get_brightness"
    url = MAIN_URL + get_brightness_url

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.text)

@app.command()
def get_color_temp():
    print("Getting color temperature")
    """
    curl -X 'GET' \
    'http://127.0.0.1:8000/get_color_temp' \
    -H 'accept: application/json'
    """

    get_color_temp_url = "/get_color_temp"
    url = MAIN_URL + get_color_temp_url

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    app()