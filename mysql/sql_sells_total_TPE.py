import mysql.connector
import xlrd
import time
import sys
sys.path.append("lib/")
from myio import read_excel, save

def SQL_SELLS_TOTAL_TPE():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database="storemanager"
    )
    mycursor = mydb.cursor()

    # check if table exists
    sql = "SHOW TABLES LIKE 'sells_total_rows_TPE'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        sql = "DROP TABLE sells_total_rows_TPE"
        mycursor.execute(sql)

    sql = "CREATE TABLE sells_total_rows_TPE (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT(255), addr VARCHAR(255), area VARCHAR(255), price VARCHAR(255), url VARCHAR(255))"
    mycursor.execute(sql)


    house_sheet = read_excel("sells/data/TPE/info/total_rows_TPE.xlsx")

    sql = "INSERT INTO sells_total_rows_TPE (post_id, addr, area, price, url) VALUES (%s, %s, %s, %s, %s)"
    for data in house_sheet:
        post_id = data["post_id"]
        addr = data["addr"]
        area = data["area"]
        price = data["price"]
        url = data["url"]

        val = (post_id, addr, area, price, url)
        print(val)
        mycursor.execute(sql, val)

    mydb.commit()
    print("Sells total rows TPE complete")
    time.sleep(1.0)
