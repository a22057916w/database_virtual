import os
import mysql.connector
import xlrd
import time

def SQL_SELLS_IMG():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database="storemanager"
    )
    mycursor = mydb.cursor()

    # ******************************************* dealing TPE images *****************************
    # check if table exists
    sql = "SHOW TABLES LIKE 'sells_img_TPE'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        sql = "DROP TABLE sells_img_TPE"
        mycursor.execute(sql)

    sql = "CREATE TABLE sells_img_TPE (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT(255), directory VARCHAR(255))"
    mycursor.execute(sql)

    sql = "INSERT INTO sells_img_TPE (post_id, directory) VALUES (%s, %s)"

    dir = r"C:\xampp\htdocs\img\sells\TPE/"
    result = os.listdir(path = dir)
    for p in result:
        post_id = p
        path = os.path.join(dir, p)
        val = (post_id, path)
        print(val)
        mycursor.execute(sql, val)

    mydb.commit()
    print("Sells TPE images complete")
    # ******************************************* dealing NTC images *****************************
    # check if table exists
    sql = "SHOW TABLES LIKE 'sells_img_NTC'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        sql = "DROP TABLE sells_img_NTC"
        mycursor.execute(sql)

    sql = "CREATE TABLE sells_img_NTC (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT(255), directory VARCHAR(255))"
    mycursor.execute(sql)

    sql = "INSERT INTO sells_img_NTC (post_id, directory) VALUES (%s, %s)"

    dir = r"C:\xampp\htdocs\img\sells\NTC/"
    result = os.listdir(path = dir)
    for p in result:
        post_id = p
        path = os.path.join(dir, p)
        val = (post_id, path)
        print(val)
        mycursor.execute(sql, val)

    mydb.commit()
    print("Sells NTC images complete")
    mydb.close()
