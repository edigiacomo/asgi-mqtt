import logging

import paho.mqtt.client as mqtt


logger = logging.getLogger(__name__)


def on_connect(client, userdata, rc):
    logger.info("Connected with status {}".format(rc))
    client.subscribe("#")


def on_message(client, userdata, message):
    logger.debug("Received message from topic {}".format(message.topic))
    channel = userdata["channel"]
    channel.send("mqtt.subscribe", {
        "topic": message.topic,
        "payload": message.payload,
        "qos": message.qos,
        "host": userdata["host"],
        "port": userdata["port"],
    })


class Server(object):
    def __init__(self, channel, host, port):
        self.channel = channel
        self.host = host
        self.port = port
        self.client = mqtt.Client(userdata={
            "channel": self.channel,
            "host": self.host,
            "port": self.port,
        })
        self.client.on_connect = on_connect
        self.client.on_message = on_message

    def run(self):
        self.client.connect(self.host, self.port)
        self.client.loop_forever()
