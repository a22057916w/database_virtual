import googlemaps
import ast
import sys
import time
import requests
import json
sys.path.append("lib/")
from myio import read_excel, save

def findPlaces(locations, types, pagetoken = None):
    vic = [] # to save result of the vicinity
    cnt = 0
    for loc in locations:
        dicLoc = ast.literal_eval(loc["coordinate"]) # turn string into dict
        coord = (dicLoc["lat"], dicLoc["lng"]) # make a coordinate
        lat = dicLoc["lat"]
        lng = dicLoc["lng"]
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "," + str(lng) + "&radius=150&type=parking&key=AIzaSyDcixkMKgROY2tE_4VLPTioPtDOwbmzfcI"
        print(url)
        response = requests.get(url)
        res = json.loads(response.text)
        # print(res)
        print("here results ---->>> ", len(res["results"]))

        for result in res["results"]:
            info = ";".join(map(str,[result["name"],result["geometry"]["location"]["lat"],result["geometry"]["location"]["lng"],result.get("rating",0),result["place_id"]]))
            print(info)
            pagetoken = res.get("next_page_token",None)

        print("here -->> ", pagetoken)

    return pagetoken


if __name__ == "__main__":
    gmaps = googlemaps.Client(key = "AIzaSyDcixkMKgROY2tE_4VLPTioPtDOwbmzfcI")

    # read location information
    leaseTPE = read_excel("lease/data/TPE/geo/coordinate/loc_TPE.xlsx")
    leaseNTC = read_excel("lease/data/NTC/geo/coordinate/loc_NTC.xlsx")
    sellsTPE = read_excel("sells/data/TPE/geo/coordinate/loc_TPE.xlsx")
    sellsNTC = read_excel("sells/data/NTC/geo/coordinate/loc_NTC.xlsx")

    # set directry
    fname = ["lease/data/TPE/geo/general/", "lease/data/NTC/geo/general/",
    "sells/data/TPE/geo/general/", "sells/data/NTC/geo/general/"]

    locList = [leaseTPE, leaseNTC, sellsTPE, sellsNTC]
    types = ["bus_station", "parking"] # types need to be search for
    vic = [] # a list of naerby facilities
    cnt = 0 # a counter for the locList loop
    pagetoken = None
    while True:
        pagetoken = findPlaces(leaseTPE, "parking", pagetoken=pagetoken)
        time.sleep(5)

        if not pagetoken:
            break
