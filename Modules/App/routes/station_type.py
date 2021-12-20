from os import curdir
import requests
import json
import psycopg2

from flask import Flask, Blueprint, jsonify, request
# from werkzeug.wrappers import response
from . import api
from App.db import conn
# from ..helpers import validSchema 

@api.route("/StationType/<int:id_station_type>", methods=["GET"])
@api.route("/StationType", methods=["GET"])
def StationTypeGet(id_station_type=None):
    _text = "" if not id_station_type  else f" where id_station_type={id_station_type}"
    try:
        cur = conn.cursor()
        cur.execute(f"select * from station_types {_text}")
        res = cur.fetchall()
        _d = [i[0] for i in cur.description]
        _result = [dict(zip(_d, i)) for i in res]
        return jsonify(_result)
    except Exception as Err:
        return f"Error!!! {Err}", 410

@api.route("/StationType", methods=["POST"])
def StationTypePost():
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        cur.execute("insert into station_types (name, descr) values (%(name)s, %(descr)s) returning  id_station_type", _data)
        id_last = cur.fetchone()[0]
        conn.commit()
        return f"{id_last}"
    except Exception as Err:
        conn.rollback()
        return f"Error!!! {Err}", 411
    
@api.route("/StationType/<int:id_station_type>", methods=["PUT"])
def StationTypePut(id_station_type):
    print(id_station_type)
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        res = cur.execute(f"update station_types set name=%(name)s , descr=%(descr)s where id_station_type = {id_station_type} returning  id_station_type", _data)
        id_last = cur.fetchone()[0]

        conn.commit()
        return f"{id_last}"
    except psycopg2.DatabaseError as Err:
        conn.rollback()
        return f"Error!!! {Err}", 412
    except TypeError as Err:
        conn.rollback()
        return f"Error!!! No data.", 413

@api.route("/StationType/<int:id_station_type>", methods=["DELETE"])
def StationTypeDelete(id_station_type):
    print(id_station_type)
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    try:
        cur = conn.cursor()
        cur.execute(f"delete from station_types where id_station_type = {id_station_type}  returning  id_station_type")
        cur.fetchone()[0]
        conn.commit()
        return f"Ok"
    except Exception as Err:
        conn.rollback()
        return f"Error! No data.", 414

