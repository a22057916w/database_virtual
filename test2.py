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

house_sheet = read_excel("lease/data/TPE/info/info_box_TPE.xlsx")


mycursor = mydb.cursor()

# check if table exists
stmt = "SHOW TABLES LIKE 'lease_house_info_TPE'"
mycursor.execute(stmt)
result = mycursor.fetchone()
if result:
    # there is a table named "tableName"
    print("table already exists")
else:
    # there are no tables named "tableName"
    sql = "CREATE TABLE lease_house_info_TPE (post_id INT(255)  PRIMARY KEY, 坪數 VARCHAR(255), 型態 VARCHAR(255), 樓層 VARCHAR(255), 權狀坪數 VARCHAR(255), 現況 VARCHAR(255), 社區 VARCHAR(255))"
    mycursor.execute(sql)

sql = "INSERT INTO lease_house_info_TPE (post_id, 坪數, 型態, 樓層, 權狀坪數, 現況, 社區) VALUES (%s, %s, %s, %s, %s, %s, %s)"

tmp = 0
for data in house_sheet:
    post_id = tmp

    tmp = tmp + 1

    area = type = floor = owner_area = now = com = "NULL"
    """post_id = data["post_id"]
    area = data["坪數"]
    type = data["型態"]
    floor = data["樓層"]
    owner_area = data["權狀坪數"]
    now = data["現況"]
    com = data["社區"]"""

    val = (post_id, area, type, floor, owner_area, now, com)
    print(val)
    mycursor.execute(sql, val)
