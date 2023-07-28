from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./index.html")


@app.route("/get_station_info/<station_keyword>", methods=["GET"])
def get_station_info(station_keyword):
    return station_keyword


if __name__ == "__main__":
    app.run()
