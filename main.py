# main.py
# This file contains the Cloud Run Function entrypoint.
# Cloud Run Functions will automatically call the "main" function
# whenever an HTTP request is received.
# The "request" object works like Flask's request:
#   - request.args for query parameters
#   - request.json for JSON body
#   - request.headers for headers
# You must return either:
#   - a string
#   - a dict (auto-converted to JSON)
#   - a tuple (body, status_code)
# No server code, no Flask app, no container code required.

# Cloud Run Functions only gives you ONE entrypoint function ("main"),
# but you can create multiple endpoints by checking request.path.
# This behaves like a tiny router.

def main(request):
    path = request.path  # e.g. "/", "/status"

    # Default endpoint: return HTML
    if path == "/" or path == "":
        html = """
        <html>
            <head><title>Cloud Run Functions</title></head>
            <body>
                <h1>Hello Steve!</h1>
                <p>This is your HTML endpoint running on Cloud Run Functions.</p>
            </body>
        </html>
        """
        # Return HTML with correct content type
        return html, 200, {"Content-Type": "text/html"}

    # Endpoint 2: /status  (JSON response)
    if path == "/status":
        return {
            "status": "ok",
            "service": "cloud-run-functions"
            "version": "1.0"
        }

    # Default fallback for unknown paths
    return {"error": "Unknown endpoint", "path": path}, 404
