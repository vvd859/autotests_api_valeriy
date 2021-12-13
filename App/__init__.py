from flask import Flask, Blueprint
from .routes import api
from db import conn

app = Flask(__name__)

# app.register_blueprint(routes.station_type, url_prefix="/api")
app.register_blueprint(routes.api, url_prefix="/api")

@app.route("/")
def index():
    return "Index"