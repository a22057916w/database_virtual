import sys
sys.path.append("lib/")
from wb import get_web_page
from bs4 import BeautifulSoup
from myio import read_excel, save
from progress_bar import progress, showProgess
import time
import os
import re
import urllib.request
import json
import pandas as pd
import shutil

DETAIL_URL = "https://sale.591.com.tw/home/house/detail/2/"
urlJumpIp = 3

def save(img_urls, post_id, dir):
    if img_urls:
        try:
            dname = dir + str(post_id)
            os.makedirs(dname, exist_ok=True)

            cnt = 0         # Counter for photos
            for img_url in img_urls:
                fname = str(cnt) + ".jpg"
                urllib.request.urlretrieve(img_url, os.path.join(dname, fname))
                cnt = cnt + 1

        except Exception as e:
            print(e)

def get_images(dom):
    soup = BeautifulSoup(dom, "html.parser")
    try:
        div = soup.find("div", "img_list")
        images = div.find_all("img")

        img_urls = []
        for img in images:
            img_urls.append(img["src"].replace("118x88.crop", "730x460"))

        return img_urls
    except Exception as e:
        print("Webpage is not exists")
        return None



def IMG_NTC_INIT():
    row_data = read_excel("sells/data/NTC/info/total_rows_NTC.xlsx") # get the excel info

    dir = r"C:\xampp\htdocs\img\sells\NTC/"
    if os.path.exists(dir): # 先刪除原本的images資料夾
        shutil.rmtree(dir, ignore_errors=True)

    for data in row_data:
        page = get_web_page(DETAIL_URL + data["url"], urlJumpIp)
        img_urls = get_images(page)
        save(img_urls, data["post_id"], dir)
        showProgess(__file__)

    print(str(__file__) + " complete")
