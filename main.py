# Import Flask and jsonify helper
# Flask is a lightweight web framework that Cloud Run can run easily.
from flask import Flask, jsonify
from datetime import datetime

# Create the Flask application object.
# This represents your web service.
app = Flask(__name__)

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
            &nbsp;&nbsp;One other path is served: "/status"
        </p>
            <ul>
                <li>Github Repo: <a href="https://github.com/wizzard262/python-server">https://github.com/wizzard262/python-server</a>
                <li>Github Repo README (setup): <a href="https://github.com/wizzard262/python-server/blob/main/README.md">https://github.com/wizzard262/python-server/blob/main/README.md</a>
                <li>Homepage URL: <a href="https://python-server-git-576465670226.europe-west1.run.app/">https://python-server-git-576465670226.europe-west1.run.app/</a>
                <li>Status URL (JSON): <a href="https://python-server-git-576465670226.europe-west1.run.app/status">https://python-server-git-576465670226.europe-west1.run.app/status</a>
                <li>Console Service URL: <a href="https://console.cloud.google.com/run/detail/europe-west1/python-server-git/observability/metrics?project=my-project-1491071384075">https://console.cloud.google.com/run/detail/europe-west1/python-server-git/observability/metrics?project=my-project-1491071384075</a>
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
