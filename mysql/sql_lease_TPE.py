import mysql.connector
import xlrd
import time
import sys
sys.path.append("lib/")
from myio import read_excel, save

def SQL_LEASE_TPE():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database="storemanager"
    )

    mycursor = mydb.cursor()
    # check if table exists
    sql = "SHOW TABLES LIKE 'lease_house_info_TPE'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        sql = "DROP TABLE lease_house_info_TPE"
        mycursor.execute(sql)

    sql = "CREATE TABLE lease_house_info_TPE (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT(255), 坪數 VARCHAR(255), 型態 VARCHAR(255), 樓層     VARCHAR(255), 權狀坪數 VARCHAR(255), 現況 VARCHAR(255), 社區 VARCHAR(255), 房屋資料 VARCHAR(255), 生活機能 VARCHAR(255), 附近交通 VARCHAR(255))"
    mycursor.execute(sql)


    # ************************** lease info box TPE ****************************************
    house_sheet = read_excel("lease/data/TPE/info/info_box_TPE.xlsx")

    sql = "INSERT INTO lease_house_info_TPE (post_id, 坪數, 型態, 樓層, 權狀坪數, 現況, 社區) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    for data in house_sheet:
        post_id = data["post_id"]
        area = data["坪數"]
        type = data["型態"]
        floor = data["樓層"]
        owner_area = data["權狀坪數"]
        now = data["現況"]
        com = data["社區"]

        val = (post_id, area, type, floor, owner_area, now, com)
        print(val)
        mycursor.execute(sql, val)

    mydb.commit()
    print("Lease info box TPE complete")
    time.sleep(1.0)

    # ******************************** lease house box TPE **********************************
    house_sheet = read_excel("lease/data/TPE/info/house_box_TPE.xlsx")

    sql = "UPDATE lease_house_info_TPE SET 房屋資料 = %s, 生活機能 = %s, 附近交通 = %s WHERE post_id = %s"
    for data in house_sheet:
        post_id = data["post_id"]
        house_data = data["房屋資料"]
        life_func = data["生活機能"]
        traffic = data["附近交通"]

        val = (house_data, life_func, traffic, post_id)
        mycursor.execute(sql, val)
        print(post_id, val)

    mydb.commit()
    print("Lease house box TPE complete")
