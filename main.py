from pathlib import Path


INDEX_FILE = Path(__file__).with_name("index.html")


def app(environ, start_response):
    """Serve the portfolio as a small WSGI application for Vercel."""
    if environ.get("REQUEST_METHOD") != "GET":
        start_response("405 Method Not Allowed", [("Allow", "GET")])
        return [b"Method Not Allowed"]

    if environ.get("PATH_INFO", "/") not in {"", "/", "/index.html"}:
        start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
        return [b"Not Found"]

    body = INDEX_FILE.read_bytes()
    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ],
    )
    return [body]