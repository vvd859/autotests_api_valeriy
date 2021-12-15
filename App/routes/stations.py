from os import curdir
import requests
import json

from flask import Flask, Blueprint, jsonify, request
# from werkzeug.wrappers import response
from . import api
from db import conn
# from ..helpers import validSchema 

@api.route("/Station/<int:id_station>", methods=["GET"])
@api.route("/Station", methods=["GET"])
def StationGet(id_station=None):
    _text = "" if not id_station  else f" where id_station={id_station}"
    cur = conn.cursor()
    res = cur.execute(f"select * from stations {_text}")
    res = cur.fetchall()
    # for i in res.fetchall():
    _d = [i[0] for i in cur.description]
    print(_d)
    print (res)
    _result = []
    for i in res:
        _result.append(dict(zip(_d, i)))
    return jsonify(_result)

@api.route("/Station/Type/<int:id_station_type>", methods=["GET"])
def StationTypesGet(id_station_type=None):
    _text = "" if not id_station_type  else f" where id_station_type={id_station_type}"
    cur = conn.cursor()
    res = cur.execute(f"select * from stations {_text}")
    res = cur.fetchall()
    # for i in res.fetchall():
    _d = [i[0] for i in cur.description]
    print(_d)
    print (res)
    _result = []
    for i in res:
        _result.append(dict(zip(_d, i)))
    return jsonify(_result)

@api.route("/Station", methods=["POST"])
def StationPost():
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        res = cur.execute("insert into stations (id_station_type, name, descr) values (%(id_station_type)s, %(name)s, %(descr)s)", _data)
        conn.commit()
        return f"fdgsdfgs\n{res}"
    except Exception as Err:
        conn.rollback()
        return f"Error!!! {Err}"
    
@api.route("/Station/<int:id_station>/<int:id_station_type>", methods=["PUT"])
def StationPut(id_station, id_station_type):
    print(id_station, id_station_type)
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        res = cur.execute(f"update stations set name=%(name)s, descr=%(descr)s where id_station = {id_station} and id_station_type ={id_station_type}", _data)
        conn.commit()
        return f"fdgsdfgs\n{res}"
    except Exception as Err:
        print(cur.query)
        conn.rollback()
        return f"Error!!! {Err}"

@api.route("/Station/<int:id_station>", methods=["DELETE"])
def StationDelete(id_station):
    print(id_station)
    # with open("App/schemas/station_types.json", "r") as _f:
    #     _schema = json.load(_f)

    _data = request.get_json()
    try:
        cur = conn.cursor()
        res = cur.execute(f"delete from stations where id_station = {id_station}")
        conn.commit()
        return f"fdgsdfgs\n{res}"
    except Exception as Err:
        print(cur.query)
        conn.rollback()
        return f"Error!!! {Err}"

