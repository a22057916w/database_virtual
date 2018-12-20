import mysql.connector
import xlrd
import time
import sys
sys.path.append("lib/")
from myio import read_excel, save

def SQL_SELLS_NTC():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database="storemanager"
    )

    mycursor = mydb.cursor()
    # check if table exists
    sql = "SHOW TABLES LIKE 'sells_house_info_NTC'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        sql = "DROP TABLE sells_house_info_NTC"
        mycursor.execute(sql)

    sql = "CREATE TABLE sells_house_info_NTC (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT(255), 坪數 VARCHAR(255), 型態 VARCHAR(255), 樓層     VARCHAR(255), 社區 VARCHAR(255), 屋齡 VARCHAR(255), 坪數說明 VARCHAR(255), 房屋資料 VARCHAR(255), 生活機能 VARCHAR(255), 附近交通 VARCHAR(255))"
    mycursor.execute(sql)


    # ************************** lease info box NTC ****************************************
    house_sheet = read_excel("sells/data/NTC/info/info_box_NTC.xlsx")

    sql = "INSERT INTO sells_house_info_NTC (post_id, 坪數, 型態, 樓層, 社區, 屋齡) VALUES (%s, %s, %s, %s, %s, %s)"
    for data in house_sheet:
        post_id = data["post_id"]
        area = data["area"]
        age = data["age"]
        floor = data["floor"]
        com = data["community"]
        type = data["form"]

        val = (post_id, area, type, floor, com, age)
        print(val)
        mycursor.execute(sql, val)

    mydb.commit()
    print("Sells info box NTC complete")
    time.sleep(1.0)

    # ******************************** lease house box NTC **********************************
    house_sheet = read_excel("sells/data/NTC/info/house_box_NTC.xlsx")

    sql = "UPDATE sells_house_info_NTC SET 坪數說明 = %s, 房屋資料 = %s, 生活機能 = %s, 附近交通 = %s WHERE post_id = %s"
    for data in house_sheet:
        post_id = data["post_id"]
        area_info = data["坪數說明"]
        house_data = data["房屋資料"]
        life_func = data["生活機能"]
        traffic = data["附近交通"]

        val = (area_info, house_data, life_func, traffic, post_id)
        mycursor.execute(sql, val)
        print(post_id, val)

    mydb.commit()
    print("Sells house box NTC complete")
