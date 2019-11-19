#!/usr/bin/env python
"""
    File 	        : database.py
    Package         :
    Description     : This is use for connecting mysql database and running sql query.
    Project Name    : FLASK REST API
    Created by Avinash on 18/11/2019
"""

import mysql.connector
import time
from utility import *
import traceback


class DataBase(Utility):
    """
    Class which Hold Database connectivity and executing query
    """
    module_name = "DataBase"

    def __init__(self):
        self.connection_obj = None
        Utility.__init__(self)
        self.create_connection_obj()

    def create_connection_obj(self):
        try:
            self.connection_obj = mysql.connector.connect(**self.connection_details)
            self.connection_obj.autocommit = True
            print "connected to db", self.connection_obj
        except Exception, ex:
            print "DBCONNECTION Exception while creating connection", ex
            self.connection_obj = None
        except:
            print "Unknown Error in MySQL connection creation" * 10
            self.connection_obj = None

    def execute_statement(self, sql_stmt, module="", parameters=(),is_insert=False):
        out = []
        st = time.time()
        split_stmt = sql_stmt.split("\n")
        sql_stmt_print = " ".join(split_stmt)

        try:
            pCur = self.connection_obj.cursor()
            retValue = pCur.execute(sql_stmt, parameters)
            if is_insert:
                out.append({"id": pCur.lastrowid})
            else:
                if pCur.description:
                    colnames = map(lambda a: a[0], pCur.description)
                    out = map(lambda a: dict(zip(colnames, a)), pCur.fetchall())
                else:
                    if retValue == -1:
                        out = []
            rows_affected = pCur.rowcount
        except Exception, e:
            print "Error in query execution %s %s (%s)" % (time.ctime(), sql_stmt_print,parameters)
            raise Exception(e)
            out = []
        split_stmt = sql_stmt.split("\n")
        sql_stmt_print = " ".join(split_stmt)
        return out

    def __del__(self):
        try:
            print "Cleaning the DB Connection ", self.connection_obj
            if self.connection_obj:
                self.connection_obj.close()
        except Exception, msg:
            print "Error in closing connection, not able to close", msg
        except:
            print "Unknown Error in closing connection, not able to close"
        print "Done Clean DB connection"
