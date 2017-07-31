import logging
import time
import signal

import paho.mqtt.client as mqtt

logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    logger.info("Connected with status {}".format(rc))
    client.subscribe("#", 2)


def on_disconnect(client, userdata, rc):
    server = userdata["server"]
    logger.info("Disconnected")
    if not server.stop:
        j = 3
        for i in range(j):
            logger.info("Trying to reconnect")
            try:
                client.reconnect()
                logger.info("Reconnected")
                break
            except Exception as e:
                if i < j:
                    logger.warn(e)
                    time.sleep(1)
                    continue
                else:
                    raise


def on_message(client, userdata, message):
    logger.debug("Received message from topic {}".format(message.topic))
    channel = userdata["channel"]
    msg = {
        "topic": message.topic,
        "payload": message.payload,
        "qos": message.qos,
        "host": userdata["host"],
        "port": userdata["port"],
    }
    try:
        channel.send("mqtt.sub", msg)
    except Exception as e:
        logger.error("Cannot send message {}".format(msg))
        logger.exception(e)


class Server(object):
    def __init__(self, channel, host, port, username=None, password=None):
        self.channel = channel
        self.host = host
        self.port = port
        self.client = mqtt.Client(userdata={
            "server": self,
            "channel": self.channel,
            "host": self.host,
            "port": self.port,
        })
        self.username = username
        self.password = password
        self.client.on_connect = on_connect
        self.client.on_disconnect = on_disconnect
        self.client.on_message = on_message

    def stop_server(self, signum, frame):
        logger.info("Received signal {}, terminating".format(signum))
        self.stop = True

    def set_signal_handlers(self):
        signal.signal(signal.SIGTERM, self.stop_server)
        signal.signal(signal.SIGINT, self.stop_server)

    def run(self):
        self.stop = False
        self.set_signal_handlers()
        if self.username:
            self.client.username_pw_set(username=self.username, password=self.password)
        self.client.connect(self.host, self.port)
        logger.info("Starting loop")
        while not self.stop:
            logger.debug("Restarting loop")
            self.client.loop()

        self.client.disconnect()
