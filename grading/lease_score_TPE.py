import re
import sys
sys.path.append("lib/")
from pdbc import MYDB
from myio import read_excel, save
from bs4 import BeautifulSoup
from wb import get_web_page
from progress_bar import progress, showProgess

def get_general(data):
    tic = []
    for d in data:
        tric = d["附近交通"].split(",")
        life = d["生活機能"].split(",")
        # For traffice data
        mrt = []            # store MRTs for each location
        els = []            # store else traffic info for each location
        for t in tric:
            if t != "NULL":
                if t.find("捷運") > 0 and t.find("公車") < 0:
                    mrt.append(t)
                else:
                    els.append(t)
        # For life function
        lif = []
        for l in life:
            if l != "NULL":
                lif.append(l)

        # Total result
        t_score = len(els) * 2
        l_score = len(lif)
        if t_score > 10:
            t_score = 10
        if l_score > 10:
            l_score = 10
        tic.append({
            "post_id": d["post_id"],
            "MRT": mrt,
            "t_else": els,
            "life": lif,
            "t_else_grade": t_score,
            "mrt_grade": "",        # Do grading later
            "life_score": l_score
        })
    return tic

def get_MRT_grade(tic, MRT):
    for t in tic:
        grade = 0
        num = len(t["MRT"])
        for i in range(0, num):         # In order to change t["MRT"][i], use range()
            mrt_exist = 0           # Check if the station exists
            for mrt in MRT:
                regex = r"(.*)" + re.escape(str(mrt["name"])) + r"(.*)" # Regular expression string
                if re.match(regex, t["MRT"][i]):        # Find matched station
                    mrt_exist = 1
                    t["MRT"][i] = mrt["name"] + "捷運站"           # Rename matched station
                    min = 3500
                    max = 35000
                    cnt = 1
                    for j in range(min, max, 3500):         # Grading for 10 class
                        if mrt["avg"] > max:
                            grade = grade + 10
                            break
                        if mrt["avg"] < j:
                            grade = grade + cnt
                            break
                        cnt = cnt + 1
                    # end i loop
                # end if
            # end mrt loop
            if mrt_exist == 0:          # Check if the station exists
                t["MRT"][i] = ""            # Delete strange station
            if num != 0:
                grade = grade / num             # Do Weighted average
        # end tm loop
        t["mrt_grade"] = grade
    # end t loop
    return tic

def LEASE_SCORE_TPE():
    TPE_data = read_excel("lease/data/TPE/info/house_box_TPE.xlsx") # get the excel house data info
    mrtOut = read_excel("MRT/mrt_out_avg.xlsx")

    tic_TPE = get_general(TPE_data)
    tic_TPE = get_MRT_grade(tic_TPE, mrtOut)
    save(tic_TPE, "lease/data/TPE/info/score_TPE")
    print(str(__file__) + " complete")
