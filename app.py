#!/usr/bin/env python
"""
    File 	        : app.py
    Package         :
    Description     :
    Project Name    : FLASK REST API
    Created by Avinash on 18/11/2019
"""

from flask import Flask, request, jsonify, make_response,render_template
import pymysql
from database import *
app = Flask(__name__)


@app.route("/")
def index():
    notes = [
     ['2019-12-21','Bundle Coli',0, -500.25],['2019-12-21','Gopalan Coli',10000, -1289.25],['2019-12-23','Bundle Coli',0, -500.25]
    ]
    total = sum(notes)
    return render_template("index.html", total = total, notes = notes)

def sum(note):
    total = 0
    for i in note:
        total += i[2]

    return total

@app.route('/api/v1.0/genes', methods=['GET'])

def get_genes():
    lookup = request.args.get('lookup', None)
    species = request.args.get('species', None)
    if lookup is None:
        return make_response(jsonify({'error': 'lookup parameter is required to fetch details', 'status': 400}),
                             400)
    if len(lookup) < 3 :
        return make_response(jsonify({'error': 'Search string length should be more than 3 characters','status': 400}), 400)
    else:
        obj = Manager()
        result = obj.get_details(lookup, species)
        print result
        return jsonify(result)

#this is to throw error which method is allow
@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Method Not found','status': 405}), 405)



class Manager(DataBase):

    def __init__(self):
        self.connection_details = {

        }
        self.read_db_config('db.config')
        print self.connection_details
        DataBase.__init__(self)

    def read_db_config(self, file_name):
        try:
            f = open(file_name, "r")
            for line in f:
                if line and not line.strip().startswith("#"):
                    key, value = line.split("=")
                    self.connection_details[key.strip()] = value.strip()
            f.close()
        except Exception, msg:
            print "Exception in readMasterConfig", msg, file_name

    def get_details(self, lookup, species):

        try:

            self.create_connection_obj()
            extra_search = ''
            lookup = '%'+lookup+'%'
            if species:
                extra_search = "and species like %s"
                params = [lookup,species]
            else:
                params = [lookup]

            sql_get_data = "select * from gene_autocomplete where display_label like %s {extra_search}"
            sql_get_data = sql_get_data.replace('{extra_search}',extra_search)
            result = self.execute_statement(sql_get_data, parameters=params)
            return result
        except Exception, msg:
            print msg
