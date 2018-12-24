import re
import sys
sys.path.append("lib/")
from pdbc import MYDB
from myio import read_excel, save
from bs4 import BeautifulSoup
from wb import get_web_page
from progress_bar import progress, showProgess


if __name__ == " __main__":
    mydb = MYDB()
    print(mydb)
    row_data = read_excel("sells/data/TPE/info/total_rows_TPE.xlsx") # get the excel info

    #save(house_boxes, "sells/data/TPE/info/house_box_TPE")
    print(str(__file__) + " complete")
