import re
import sys
sys.path.append("lib/")
from pdbc import MYDB
from myio import read_excel, save
from bs4 import BeautifulSoup
from wb import get_web_page
from progress_bar import progress, showProgess

def get_traffic(data, MRT):
    tic = []
    for d in data:
        tric = d["附近交通"].split(",")
        mrt = []
        mrt_grd = []
        els = []
        score = 0
        for t in tric:
            print(t)
            if t.find("捷運") > 0 and t.find("公車") < 0:
                tmp, grade = get_MRT_grade(t, MRT)
                mrt.append(tmp)
                mrt_grd.append(grade)
            else:
                els.append(t)

        for g in mrt_grd:
            score = score + g
        if len(mrt_grd) != 0:
            score = score / len(mrt_grd)

        tic.append({
            "post_id": d["post_id"],
            "MRT": mrt,
            "t_else": els,
            "t_else_score": len(els) * 2,
            "mrt_score": score
        })

    return tic

def get_MRT_grade(t, MRT):
    grade = 0
    for mrt in MRT:
        regex = r"(.*)" + re.escape(str(mrt["name"])) + r"(.*)" #regular expression string
        print(t, " ", type(t))
        if re.match(regex, t):
            t = mrt["name"] + "捷運站"
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
        else:
            t = None

    return t, grade

#def GTEST():
if __name__ == "__main__":
    TPE_data = read_excel("sells/data/TPE/info/house_box_TPE.xlsx") # get the excel house data info
    mrtOut = read_excel("MRT/mrt_out_avg.xlsx")
    #print(mrtIn)
    print(mrtOut[0].keys())

    tic_TPE = get_traffic(TPE_data, mrtOut)
    #tic_TPE = get_MRT_grade(tic_TPE, mrtOut)
    for t in tic_TPE:
        print(t)


    #print(tic_TPE)
    #save(house_boxes, "sells/data/TPE/info/house_box_TPE")
    #print(str(__file__) + " complete")
