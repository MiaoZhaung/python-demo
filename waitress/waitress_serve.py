from waitress import serve
from flask_waitress import wsgi_app

if __name__ == "__main__":
    serve(wsgi_app, host="0.0.0.0", port=8090)
