import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class ResultConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "results_group"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        input_string = data.get('input_string', '')

        # Send instant result
        instant_result = f"Instant result for: {input_string}"
        await self.send(text_data=json.dumps({
            'type': 'instant_result',
            'result': instant_result,
        }))

        # Simulate generating late results
        for i in range(1, 6):
            await asyncio.sleep(2)  # Simulates delay for late results
            late_result = f"Late result step {i} for: {input_string}"
            await self.send(text_data=json.dumps({
                'type': 'late_result',
                'result': late_result,
            }))
