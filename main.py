# Import Flask and jsonify helper
# Flask is a lightweight web framework that Cloud Run can run easily.
# jsonify does JSON formatting
# request is used to read query parameters from the URL
from flask import Flask, jsonify, request

# Imports Python’s built‑in datetime module.
from datetime import datetime

# Imports the requests library. this is for MAKING requests
import requests

# Weather code → human-readable description (WMO standard)
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}


# Create the Flask application object.
# This represents your web service.
app = Flask(__name__)

# Open-Meteo API endpoint for current weather in Berlin (latitude=52.52, longitude=13.41)
url = "https://api.open-meteo.com/v1/forecast?current_weather=true&latitude=52.52&longitude=13.41&"

# -------------------------------
# HTML ENDPOINT
# -------------------------------
# This route handles GET requests to "/".
# Cloud Run will send traffic here from root URL.
@app.route("/")
def home():
    # Returning raw HTML is fine — Flask will send it as text/html automatically.
    return """
    <html>
        <head>
            <title>Google Cloud Run service running a Flask Python web server</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
        </head>
        <body>
        <h1>Cloud Run service running a Flask Python web server</h1>
        <p>
            &nbsp;&nbsp;This homepage page is served from the Python web server.<br/>
            &nbsp;&nbsp;It also has a path to see current status: "/status"
             &nbsp;&nbsp;It also has a path to get weather: "/weather"
        </p>
            <ul>
                <li>Github Repo: <a href="https://github.com/wizzard262/python-server">https://github.com/wizzard262/python-server</a>
                <li>Github Repo README (setup): <a href="https://github.com/wizzard262/python-server/blob/main/README.md">https://github.com/wizzard262/python-server/blob/main/README.md</a>
                <li>Console Service URL: <a href="https://console.cloud.google.com/run/detail/europe-west1/python-server-git/observability/metrics?project=my-project-1491071384075">https://console.cloud.google.com/run/detail/europe-west1/python-server-git/observability/metrics?project=my-project-1491071384075</a>
            </ul>
            PATHS:
            <ul>
                <li>"/" - HTML page</li>
                <li>"/status" - JSON status endpoint</li>
                <li>"/weather?lat=53.24&lon=2.09" - JSON weather endpoint (replace lat/lon as needed, this is for Stockport, UK)</li> 
            </ul>
        </body>
    </html>
    """

# -------------------------------
# JSON ENDPOINT
# -------------------------------
# This route handles GET requests to "/status".
# jsonify() ensures proper JSON formatting and headers.
@app.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "time": datetime.utcnow().isoformat() + "Z"
    })


# -------------------------------
# WEATHER ENDPOINT
# -------------------------------
# This route handles GET requests to "/weather".
# jsonify() ensures proper JSON formatting and headers.
@app.route("/weather")
def weather():
    # Read lat/lon from query parameters
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return jsonify({"error": "Missing lat or lon"}), 400

    # Build Open-Meteo API URL
    url = (
        "https://api.open-meteo.com/v1/forecast"
        + "?latitude=" + str(lat)
        + "&longitude=" + str(lon)
        + "&current_weather=true"
    )

    # Call the API
    response = requests.get(url)
    data = response.json()

    # Extract only the current weather section
    current = data.get("current_weather")

    if not current:
        return jsonify({"error": "No current weather available"}), 404

    # Add human-readable weather description
    weather_code = current.get("weathercode")
    if weather_code is not None:
        current["weather_description"] = WEATHER_CODES.get(weather_code, "Unknown")

    return jsonify(current)    

# -------------------------------
# FLASK SERVER STARTUP
# -------------------------------
# Cloud Run sets the PORT environment variable automatically.
# Buildpacks expect your app to listen on this port.
# DO NOT hardcode port numbers — always read from $PORT.
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # fallback for local testing
    # host="0.0.0.0" makes the server reachable from Cloud Run's network.
    app.run(host="0.0.0.0", port=port)
