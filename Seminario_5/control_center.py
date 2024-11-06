import paho.mqtt.client as mqtt
import asyncio
import json
import aiocoap
import threading

class ControlCenter:
    def __init__(self):
        # MQTT setup
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect("localhost", 1883, 60)
        
        # Temperature threshold
        self.temp_threshold = 25
        
    def on_message(self, client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            print(f"Received sensor data: {data}")
            
            # Check temperature and control thermostat
            if data["temperature"] > self.temp_threshold:
                asyncio.run(self.control_thermostat("on", data["temperature"]))
            else:
                asyncio.run(self.control_thermostat("off", data["temperature"]))
                
        except Exception as e:
            print(f"Error processing message: {e}")

    async def control_thermostat(self, power, temperature):
        context = await aiocoap.Context.create_client_context()
        
        payload = json.dumps({
            "power": power,
            "temperature": temperature
        }).encode('utf8')
        
        request = aiocoap.Message(
            code=aiocoap.PUT,
            payload=payload,
            uri='coap://localhost/thermostat'
        )
        
        try:
            response = await context.request(request).response
            print(f"Thermostat response: {response.payload.decode()}")
        except Exception as e:
            print(f"Failed to update thermostat: {e}")
            
    def run(self):
        self.mqtt_client.subscribe("home/environment")
        self.mqtt_client.loop_forever()

if __name__ == "__main__":
    control_center = ControlCenter()
    try:
        control_center.run()
    except KeyboardInterrupt:
        print("Control center stopped")