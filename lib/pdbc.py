import os
import mysql.connector
import xlrd
import time


def MYDB():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database="storemanager"
    )
    return mydb
