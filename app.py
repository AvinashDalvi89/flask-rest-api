#!/usr/bin/env python
"""
    File 	        : app.py
    Package         :
    Description     :
    Project Name    : FLASK REST API
    Created by Avinash on 18/11/2019
"""

from flask import Flask, request, jsonify, make_response
import pymysql
from database import *
app = Flask(__name__)

def index():
    return "Hello Nuclear Geeks"

@app.route('/api/v1.0/genes', methods=['GET'])

def get_genes():
    lookup = request.args.get('lookup', None)
    species = request.args.get('species', None)
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
            'host': 'ensembldb.ensembl.org',
            'database': 'ensembl_website_97',
            'user': 'anonymous',
            'password': ''
        }
        DataBase.__init__(self)

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
