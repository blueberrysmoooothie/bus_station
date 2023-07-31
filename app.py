from flask import Flask, render_template
from models import BusStation

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./index.html")


@app.route("/get_station_info/<station_keyword>", methods=["GET"])
def get_station_info(station_keyword):
    return BusStation.search_station(station_keyword)


@app.route("/get_bus_info/<station_id>", methods=["GET"])
def get_bus_info(station_id):
    bus_info = BusStation.get_bus_info(station_id)
    return bus_info


if __name__ == "__main__":
    app.run()
