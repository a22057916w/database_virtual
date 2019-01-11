import re
import sys
sys.path.append("lib/")
from myio import read_excel, save
from bs4 import BeautifulSoup
from wb import get_web_page
from progress_bar import progress, showProgess

DETAIL_URL = "https://sale.591.com.tw/home/house/detail/2/"
urlJumpIp = 1


def get_host_box(dom, post_id):
    info_boxes = []
    name = "邱先生"
    phone = "0930210924"
    try:
        soup = BeautifulSoup(dom, "html.parser")
        host_box = soup.find("div", "info-box-host")
        name = host_box.find("span", "info-span-name").string + host_box.find("span", "info-span-msg").string
        phone = host_box.find("span", "info-host-word").string.replace(" ", "").replace("\n", "")
    except:
        pass

    info_boxes.append({
        "post_id": post_id,
        "name": name,
        "phone": phone
    })

    return info_boxes

if __name__ == "__main__":
    row_data = read_excel("sells/data/TPE/info/total_rows_TPE.xlsx") # get the excel info

    host_boxes = []
    for data in row_data:
        page = get_web_page(DETAIL_URL + data["url"], urlJumpIp)
        host_boxes += get_host_box(page, data["post_id"])

        showProgess(__file__)

    save(host_boxes, "sells/data/TPE/info/host_box_TPE")
    print(str(__file__) + " complete")
