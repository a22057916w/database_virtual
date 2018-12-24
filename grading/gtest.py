import re
import sys
sys.path.append("lib/")
from pdbc import MYDB
from myio import read_excel, save
from bs4 import BeautifulSoup
from wb import get_web_page
from progress_bar import progress, showProgess


def GTEST():

    house_data = read_excel("sells/data/TPE/info/house_box_TPE.xlsx") # get the excel house data info
    mrtOut = read_excel("MRT/mrt_out_avg.xlsx")
    #print(mrtIn)
    print(mrtOut[0].keys())
    print(house_data[0].keys())
    print(house_data[1]["附近交通"])

    tic_TPE = []
    for data in house_data:
        strs = data["附近交通"].split(",")
        mrt = []
        alt = []
        for s in strs:
            if s.find("捷運") > 0:
                mrt.append(s)
            else:
                alt.append(s)
        tic_TPE.append({
            "post_id": data["post_id"],
            "MRT": mrt,
            "alt": alt
        })

    print(tic_TPE)
    #save(house_boxes, "sells/data/TPE/info/house_box_TPE")
    print(str(__file__) + " complete")

print("2343214324")


"""mydb = MYDB()
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM mrt_in_avg")
result = mycursor.fetchall()
for x in result:
    print(x)
print(type(result))
print(result[0].keys())"""
