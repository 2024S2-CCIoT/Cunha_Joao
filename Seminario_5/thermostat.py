import asyncio
import aiocoap.resource as resource
import aiocoap
import json

class ThermostatResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.state = {"power": "off", "temperature": 22}

    async def render_get(self, request):
        payload = json.dumps(self.state).encode('utf8')
        return aiocoap.Message(payload=payload)

    async def render_put(self, request):
        try:
            new_state = json.loads(request.payload.decode('utf8'))
            self.state.update(new_state)
            payload = json.dumps(self.state).encode('utf8')
            print(f"Thermostat state updated: {self.state}")
            return aiocoap.Message(payload=payload)
        except Exception as e:
            return aiocoap.Message(code=aiocoap.INTERNAL_SERVER_ERROR)

async def main():
    root = resource.Site()
    root.add_resource(['thermostat'], ThermostatResource())
    
    await aiocoap.Context.create_server_context(root, bind=('localhost', 5683))
    
    try:
        await asyncio.get_running_loop().create_future()
    except KeyboardInterrupt:
        print("Thermostat server stopped")

if __name__ == "__main__":
    asyncio.run(main())