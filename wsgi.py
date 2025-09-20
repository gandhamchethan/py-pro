from wsgiref.simple_server import make_server
from app import application

if __name__ == "__main__":
    port = 8080
    with make_server("", port, application) as httpd:
        print(f"Serving on http://127.0.0.1:8000")
        httpd.serve_forever()
