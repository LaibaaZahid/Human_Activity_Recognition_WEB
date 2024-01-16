from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("Connection req recieved")
        self.send(text_data=json.dumps({'status': 'connected'}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass
