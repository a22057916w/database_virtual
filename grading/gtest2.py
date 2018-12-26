import googlemaps
import ast
import sys
import time
import requests
from bs4 import BeautifulSoup
sys.path.append("lib/")
from myio import read_excel, save

GOOGLE_PARKING_URL = "https://www.google.com.tw/maps/search/parking/@"

def get_web_page(url):
    time.sleep(0.5)

    resp = requests.get(url=url, headers={'User-Agent': 'Custom'})
    if resp.status_code != 200:
        print("Invalid url:", resp.url)
        return None
    else:
        return resp.text

def GTEST2():
    # read location information
    leaseTPE = read_excel("lease/data/TPE/geo/coordinate/loc_TPE.xlsx")
    page = get_web_page("https://www.openstreetmap.org/search?query=%E5%81%9C%E8%BB%8A%E5%A0%B4#map=19/25.01859/121.47618")
    print(type(page))
    soup = BeautifulSoup(page, "html.parser")
    print(soup)
    result = soup.find_all("div", "query_wrapper")
    print(result)
    
