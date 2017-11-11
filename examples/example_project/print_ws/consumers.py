import json

from channels import Group


def on_ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("mqtt").add(message.reply_channel)


def on_ws_disconnect(message):
    Group("mqtt").discard(message.reply_channel)


def on_mqtt_message(message):
    msg = "{}: {}".format(message.content["topic"],
                          message.content["payload"].decode("utf-8"))
    Group("mqtt").send({
        "text": msg
    })
