#Whit the schema.json on the sensor propaty make a class that can make a api call to the sensor and return the data that is in the keys

# The class should have a method that takes a json file as input and returns the data that is in the keys

import time


class Sensor:
    def __init__(self, keys, TypeOfAPI, APIVersion, IP, Port, BasePath):
        self.keys = keys
        self.TypeOfAPI = TypeOfAPI
        self.APIVersion = APIVersion
        self.IP = IP
        self.Port = Port
        self.BasePath = BasePath

    def process_data(self, data):
        result = {}
        for key in self.schema:
            result[key] = data[key]
        return result
    
  
    def mock_call(self):
        print("MAKING API CALL TO SENSOR")
        time.sleep(1)
        # Return only the important information from the sensor data
        return self.keys