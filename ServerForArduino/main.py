#!/usr/bin/python3
"""Main page for Arduino"""
from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import time
import csv

app = Flask(__name__)
api = Api(app)

args_get = reqparse.RequestParser()
args_get.add_argument("t", default=None, type=float)
args_get.add_argument("h", default=None, type=float)
args_get.add_argument("p", default=None, type=float)

# api
class SensorsData(Resource):
    def get(self):
        args = args_get.parse_args()
        # with open("data", "a") as data:
        #     data.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}: {args}\n")
        with open("data.csv", "a", newline="") as csv_file:
        	file_writer = csv.writer(csv_file, delimiter=";")
        	file_writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), args["t"], args["h"], args["p"]])
        return args, 200

api.add_resource(SensorsData, "/")


if __name__ == "__main__":
    host_ip = "192.168.0.102"
    app.run(host=host_ip, debug=True)