import requests
import json


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

        for station in stations_json:
            print(station)

        return stations_json

    @classmethod
    def get_bus_info(cls, stid):
        station_url = (
            "https://businfo.daegu.go.kr:8095/dbms_web_api/realtime/arr2/" + stid
        )

        bus_txt = requests.get(station_url).text
        bus_info = json.loads(bus_txt)["body"]["list"]
        # print(station_info)
        for bus in bus_info:  # stock_data는 'data' key값에 모든 정보가 들어가 있다.
            print(bus)

        return bus_info
