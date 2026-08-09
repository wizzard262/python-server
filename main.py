# Import Flask and jsonify helper
# Flask is a lightweight web framework that Cloud Run can run easily.
from flask import Flask, jsonify

# Create the Flask application object.
# This represents your web service.
app = Flask(__name__)

# -------------------------------
# HTML ENDPOINT
# -------------------------------
# This route handles GET requests to "/".
# Cloud Run will send traffic here when someone visits your root URL.
@app.route("/")
def home():
    # Returning raw HTML is fine — Flask will send it as text/html automatically.
    return """
    <html>
        <head><title>Cloud Run Flask</title></head>
        <body>
            <h1>Hello Steve!</h1>
            <p>This is your HTML endpoint running in Flask on Cloud Run.</p>
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
    return jsonify({"status": "ok"})

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
