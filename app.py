def application(environ, start_response):
    response_body = b"Hello, WSGI World!"
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body)))
    ]
    start_response(status, headers)
    return [response_body]
