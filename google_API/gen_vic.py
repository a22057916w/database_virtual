import googlemaps
import ast
import sys
import time
sys.path.append("lib/")
from myio import read_excel, save

def get_geoNearBy(locations, types):
    vic = [] # to save result of the vicinity
    cnt = 0
    for loc in locations:
        dicLoc = ast.literal_eval(loc["coordinate"]) # turn string into dict
        coord = (dicLoc["lat"], dicLoc["lng"]) # make a coordinate

        # search the landmarks in the vicinity
        time.sleep(10.0)
        result = gmaps.places_nearby(location = coord, radius = 1000, type = types, language = "zh-TW")
        for rst in result["results"]:
            #dist_info = gmaps.distance_matrix(loc["addr"], rst["name"], mode = "walking")
            vic.append({
                "addr": loc["addr"],
                "name": rst["name"],
                #"rating": rst["rating"]
                #"dist": dist_info["rows"][0]["elements"][0]["distance"]["value"],
                #"time": dist_info["rows"][0]["elements"][0]["duration"]["value"]
            })
        print(cnt)
        cnt = cnt + 1

    return vic

if __name__ == "__main__":
    gmaps = googlemaps.Client(key = "AIzaSyDcixkMKgROY2tE_4VLPTioPtDOwbmzfcI")

    # read location information
    leaseTPE = read_excel("lease/data/TPE/geo/coordinate/loc_TPE.xlsx")
    leaseNTC = read_excel("lease/data/NTC/geo/coordinate/loc_NTC.xlsx")
    sellsTPE = read_excel("sells/data/TPE/geo/coordinate/loc_TPE.xlsx")
    sellsNTC = read_excel("sells/data/NTC/geo/coordinate/loc_NTC.xlsx")

    # set directry
    fname = ["lease/data/NTC/geo/general/", "lease/data/TPE/geo/general/",
    "sells/data/NTC/geo/general/", "sells/data/TPE/geo/general/"]

    locList = [leaseTPE, leaseNTC, sellsTPE, sellsNTC]
    types = ["bus_station", "parking"] # types need to be search for
    vic = [] # a list of naerby facilities
    cnt = 0 # a counter for the locList loop
    for loc in locList:
        for type in types:
            vic = get_geoNearBy(loc, type)
            print(vic)
        #save(vic, fname[cnt] + type)
        cnt = cnt + 1
