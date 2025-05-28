from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

application = DispatcherMiddleware(
    app,
    {"/server": app}
)
