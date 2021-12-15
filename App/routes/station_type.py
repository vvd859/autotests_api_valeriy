from os import curdir
import requests
import json

from flask import Flask, Blueprint, jsonify, request
# from werkzeug.wrappers import response
from . import api
from db import conn
# from ..helpers import validSchema 

@api.route("/StationType/<int:id_station_type>", methods=["GET"])
@api.route("/StationType", methods=["GET"])
def StationTypeGet(id_station_type=None):
    _text = "" if not id_station_type  else f" where id_station_type={id_station_type}"
    cur = conn.cursor()
    res = cur.execute(f"select * from station_types {_text}")
    res = cur.fetchall()
    # for i in res.fetchall():
    _d = [i[0] for i in cur.description]
    print(_d)
    print (res)
    _result = []
    for i in res:
        _result.append(dict(zip(_d, i)))
    return jsonify(_result)

@api.route("/StationType", methods=["POST"])
def StationTypePost():
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        res = cur.execute("insert into station_types (name, descr) values (%(name)s, %(descr)s)", _data)
        conn.commit()
        return f"fdgsdfgs\n{res}"
    except Exception as Err:
        conn.rollback()
        return f"Error!!! {Err}", 444
    
@api.route("/StationType/<int:id_station_type>", methods=["PUT"])
def StationTypePut(id_station_type):
    print(id_station_type)
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        res = cur.execute(f"update station_types set name=%(name)s , descr=%(descr)s where id_station_type = {id_station_type}", _data)
        conn.commit()
        return f"fdgsdfgs\n{res}"
    except Exception as Err:
        print(cur.query)
        conn.rollback()
        return f"Error!!! {Err}"



@api.route("/StationType/<int:id_station_type>", methods=["DELETE"])
def StationTypeDelete(id_station_type):
    print(id_station_type)
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        res = cur.execute(f"delete from station_types where id_station_type = {id_station_type}")
        conn.commit()
        return f"fdgsdfgs\n{res}"
    except Exception as Err:
        print(cur.query)
        conn.rollback()
        return f"Error!!! {Err}"

