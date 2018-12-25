import re
import sys
sys.path.append("lib/")
from pdbc import MYDB
from myio import read_excel, save
from bs4 import BeautifulSoup
from wb import get_web_page
from progress_bar import progress, showProgess

def get_traffic(data):
    tic = []
    for d in data:
        tric = d["附近交通"].split(",")
        mrt = []
        els = []
        for t in tric:
            if t.find("捷運") > 0 and t.find("公車") < 0:
                mrt.append(t)
            else:
                els.append(t)
        tic.append({
            "post_id": d["post_id"],
            "MRT": mrt,
            "t_else": els,
            "t_else_grade": len(els) * 2,
            "mrt_grade": ""        # Do grading later
        })
    return tic

def get_MRT_grade(tic, MRT):
    for t in tic:
        grade = 0
        num = len(t["MRT"])
        for i in range(0, num):         # in order to change t["MRT"][i]
            for mrt in MRT:
                regex = r"(.*)" + re.escape(str(mrt["name"])) + r"(.*)" #regular expression string
                if re.match(regex, t["MRT"][i]):
                    t["MRT"][i] = mrt["name"] + "捷運站"
                    min = 5000
                    max = 35000
                    cnt = 1
                    for j in range(min, max, 5000):
                        if mrt["avg"] > max:
                            grade = grade + 8
                            break
                        if mrt["avg"] < j:
                            grade = grade + cnt
                            break
                        cnt = cnt + 1
                    # end i loop
                # end if
            # end mrt loop
            if num != 0:
                grade = grade / num
        # end tm loop
        t["mrt_grade"] = grade
    # end t loop
    return tic

#def GTEST():
if __name__ == "__main__":
    TPE_data = read_excel("sells/data/TPE/info/house_box_TPE.xlsx") # get the excel house data info
    mrtOut = read_excel("MRT/mrt_out_avg.xlsx")
    #print(mrtIn)
    print(mrtOut[0].keys())

    tic_TPE = get_traffic(TPE_data)
    tic_TPE = get_MRT_grade(tic_TPE, mrtOut)
    for t in tic_TPE:
        print(t)


    #print(tic_TPE)
    #save(house_boxes, "sells/data/TPE/info/house_box_TPE")
    #print(str(__file__) + " complete")
