from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
history = []

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    Ctemperature = None
    Ftemperature = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
            response = requests.get(request_url)
            if response.status_code == 200:
                data = response.json()
                weather = data["weather"][0]["description"]
                Ftemperature = round((data["main"]["temp"] - 273.15) * 9 / 5 + 32, 2)
                Ctemperature = round(data["main"]["temp"] - 273.15, 2)
                history.append(city)
            else:
                print("An error occurred.")
                Ctemperature = None
                Ftemperature = None

    return render_template("index.html", weather=weather, Ctemperature=Ctemperature,Ftemperature=Ftemperature, history=history)

if __name__ == "__main__":
    app.run(debug=True)
    
