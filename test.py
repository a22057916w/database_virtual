import os
import mysql.connector
import xlrd
import sys
sys.path.append("lib/")
from myio import read_excel, save

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="storemanager"
)

mycursor = mydb.cursor()

# check if table exists
table = 'lease_img_TPE'
stmt = "SHOW TABLES LIKE 'lease_img_TPE'"
mycursor.execute(stmt)
result = mycursor.fetchone()
if result:
    # there is a table named "tableName"
    print("table already exists")
else:
    # there are no tables named "tableName"
    sql = "CREATE TABLE lease_img_TPE (post_id INT(255)  PRIMARY KEY, directory VARCHAR(255))"
    mycursor.execute(sql)

sql = "INSERT INTO lease_img_TPE (post_id, directory) VALUES (%s, %s)"

dir = "C:/Python/database/sells/images/NTC"
result = os.listdir(path = r"C:\Python\database\sells\images\NTC")
#result = os.walk(r"D:\Python\database\sells\images\NTC")
for p in result:
    post_id = p
    path = os.path.join(dir, p)
    val = (post_id, path)
    print(val)
    mycursor.execute(sql, val)

mydb.commit()
mydb.close()
