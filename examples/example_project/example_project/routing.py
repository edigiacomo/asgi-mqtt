from channels.routing import route
from print_ws.consumers import on_ws_connect, on_ws_disconnect, on_mqtt_message


channel_routing = [
    route("websocket.connect", on_ws_connect),
    route("websocket.disconnect", on_ws_disconnect),
    route("mqtt.sub", on_mqtt_message),
]
