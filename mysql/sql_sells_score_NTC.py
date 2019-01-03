import mysql.connector
import xlrd
import time
import sys
sys.path.append("lib/")
from myio import read_excel, save

def SQL_SELLS_SCORE_NTC():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database="storemanager"
    )
    mycursor = mydb.cursor()

    # check if table exists
    sql = "SHOW TABLES LIKE 'sells_score_NTC'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        sql = "DROP TABLE sells_score_NTC"
        mycursor.execute(sql)

    sql = "CREATE TABLE sells_score_NTC (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT(255), mrt VARCHAR(255), els VARCHAR(255), life VARCHAR(255), mrt_score VARCHAR(255), t_score VARCHAR(255), l_score VARCHAR(255))"
    mycursor.execute(sql)


    house_sheet = read_excel("sells/data/NTC/info/score_NTC.xlsx")

    sql = "INSERT INTO sells_score_NTC (post_id, mrt, els, life, mrt_score, t_score, l_score) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    for data in house_sheet:
        post_id = data["post_id"]
        MRT = data["MRT"]
        els = data["t_else"]
        life = data["life"]
        mrt_score = data["mrt_grade"]
        t_score = data["t_else_grade"]
        l_score = data["life_score"]

        val = (post_id, MRT, els, life, mrt_score, t_score, l_score)
        print(val)
        mycursor.execute(sql, val)

    mydb.commit()
    print("Sells score NTC complete")
    time.sleep(1.0)
