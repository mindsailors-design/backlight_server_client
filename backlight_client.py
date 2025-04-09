import typer

app = typer.Typer()

@app.command()
def set_brightness(brightness: float):
    print(f"Setting brightness, {brightness}")
    command = """
    curl -X 'POST' \
    'http://127.0.0.1:8000/set_brightness?data=1' \
    -H 'accept: application/json' \
    -d ''
    """
    print(command)

@app.command()
def set_color_temp(color_temp: float):
    print(f"Setting color temperature: {color_temp}")
    command = """
    curl -X 'POST' \
    'http://127.0.0.1:8000/set_color_temp?data=1' \
    -H 'accept: application/json' \
    -d ''
    """
    print(command)

@app.command()
def increase_brightness():
    print("Increasing brightness")

@app.command()
def decrease_brightness():
    print("Decreasing brightness")

@app.command()
def increase_color_temp():
    print("Increasing color temperature")

@app.command()
def decrease_color_temp():
    print("Decreasing color temperature")

@app.command()
def get_brightness():
    print("Getting brightness")

@app.command()
def get_color_temp():
    print("Getting color temperature")

if __name__ == "__main__":
    app()