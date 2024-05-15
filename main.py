import json
from ServerConfig import ServerConfig
from Sensor import Sensor


def parse_json(json_file):
    with open(json_file) as f:
        data = json.load(f)

    server_config_data = data.get('serverConfig')
    server_config = ServerConfig(**server_config_data)

    sensors_data = data.get('sensors', {})
    sensors = {}
    for sensor_name, sensor_info in sensors_data.items():
        sensor = Sensor(**sensor_info)
        sensors[sensor_name] = sensor

    return server_config, sensors

json_file = './SchemaMulti.json'
server_config, sensors = parse_json(json_file)

server_config.mock_start_webserver()

keys = []
# Accessing sensor attributes
for sensor_name, sensor in sensors.items():
    print(f"Sensor: {sensor_name}")
    print(f"keys: {sensor.keys}")

    # how to convert sensor from a dictionary to a Sensor object
    sensorobj = Sensor(sensor.keys, sensor.TypeOfAPI, sensor.APIVersion, sensor.IP, sensor.Port, sensor.BasePath)


    print(type(sensorobj))

    sensorkeys = sensorobj.mock_call()
    #remove the array and add to keys
    for key in sensorkeys:
        keys.append(key)





print(keys)
# make the keys return as a json response and remove the array brackets


response = {
    "keys": keys,
    "status": 200,
    "Isconfig": "True",
    "message": "Success"
}

print(json.dumps(response))