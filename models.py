import requests
import json

# import urllib.parse as codec


class BusStation:
    def __init__(self):
        pass

    @classmethod
    def search_station(cls, searchText):
        wincId = ""
        stid_url = (
            "https://businfo.daegu.go.kr:8095/dbms_web_api/bs/search?searchText="
            + searchText
            + "&wincId="
            + wincId
        )
        json_txt = requests.get(stid_url).text
        stations_json = json.loads(json_txt)["body"]
        station_list = []
        for station in stations_json:
            station_ = {}
            station_["bsNm"] = station["bsNm"]
            station_["bsId"] = station["bsId"]
            station_["routeList"] = station["routeList"]

            station_list.append(station_)

        # for i in range(len(stations_json)):
        #     stations_json[i]['bsNm'] = codec.unquote(stations_json[i]['bsNm'])

        return station_list

    @classmethod
    def get_bus_info(cls, stid):
        station_url = (
            "https://businfo.daegu.go.kr:8095/dbms_web_api/realtime/arr2/" + stid
        )

        bus_txt = requests.get(station_url).text
        bus_info = json.loads(bus_txt)["body"]["list"]

        bus_list = []
        for bus in bus_info:
            bus_ = {}
            bus_["routeNo"] = bus["routeNo"]
            bus_["arrState"] = []
            for arr in bus["arrList"]:
                bus_["arrState"].append(arr["arrState"])

            bus_list.append(bus_)

        return bus_list
