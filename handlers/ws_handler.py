import json
import tornado.websocket

class WsHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.application.clients[id(self)] = self

    def on_message(self, message):
        try:
            coords = json.loads(message)
        except ValueError:
            return
        my_id = id(self)
        for client_id, client in self.application.clients.items():
            if my_id != client_id:
                client.write_message(json.dumps({
                    'x':         coords.get('x',0),
                    'y':         coords.get('x',0),
                    'client_id': my_id,
                }))

    def on_close(self):
        self.application.clients.pop(id(self), None)

    def check_origin(self, origin):
        return True
