from flask import Flask, Blueprint
from . import api

@api.route("/StationType", methods=["GET"])
def StationType():
    return "[get] StationType"
