import paho.mqtt.client as mqtt
import random
import time
import json

class EnvironmentalSensor:
    def __init__(self, broker="localhost", topic="home/environment"):
        self.client = mqtt.Client()
        self.broker = broker
        self.topic = topic
        
    def connect(self):
        self.client.connect(self.broker, 1883, 60)
        
    def generate_sensor_data(self):
        return {
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 80), 2),
            "light": round(random.uniform(0, 1000), 2)
        }
        
    def run(self):
        self.connect()
        while True:
            data = self.generate_sensor_data()
            self.client.publish(self.topic, json.dumps(data))
            print(f"Published: {data}")
            time.sleep(5)

if __name__ == "__main__":
    sensor = EnvironmentalSensor()
    try:
        sensor.run()
    except KeyboardInterrupt:
        print("Sensor stopped")