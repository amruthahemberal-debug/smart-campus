from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store latest sensor values
sensor_data = {
    "temp": "--",
    "humidity": "--",
    "co2": "--",
    "light": "--"
}

@app.route("/")
def home():
    return render_template("index.html", data=sensor_data)

@app.route("/update", methods=["POST"])
def update():
    global sensor_data

    sensor_data["temp"] = request.json.get("temp", "--")
    sensor_data["humidity"] = request.json.get("humidity", "--")
    sensor_data["co2"] = request.json.get("co2", "--")
    sensor_data["light"] = request.json.get("light", "--")

    return jsonify({
        "status": "success",
        "message": "Sensor data updated"
    })
    @app.route("/api/sensors")
    def get_sensors():
        return jsonify(sensor_data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
