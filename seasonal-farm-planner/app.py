from flask import Flask, render_template, jsonify
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

app = Flask(__name__, template_folder=str(BASE_DIR / "templates"), static_folder=str(BASE_DIR / "static"))


def load_json(name: str):
    path = DATA_DIR / name
    if not path.exists():
        return {}
    with path.open() as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/crop-calendar")
def crop_calendar():
    return jsonify(load_json("crop_calendar.json"))


@app.route("/api/weather")
def weather():
    return jsonify(load_json("weather_mock.json"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
