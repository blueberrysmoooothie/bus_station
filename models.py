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

        # for i in range(len(stations_json)):
        #     stations_json[i]['bsNm'] = codec.unquote(stations_json[i]['bsNm'])

        return stations_json

    @classmethod
    def get_bus_info(cls, stid):
        station_url = (
            "https://businfo.daegu.go.kr:8095/dbms_web_api/realtime/arr2/" + stid
        )

        bus_txt = requests.get(station_url).text
        bus_info = json.loads(bus_txt)["body"]["list"]
        # print(station_info)
        # for i in range(len(bus_info)):
        #     bus_info[i]['bsNm'] = codec.unquote(bus_info[i]['bsNm'])

        return bus_info
