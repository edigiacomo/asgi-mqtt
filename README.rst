asgimqtt
========

``asgimqtt`` is a simple `MQTT <http://mqtt.org/>`_ interface for `ASGI
<http://channels.readthedocs.org/en/latest/asgi.html>`_.


Usage
-----

Connect the server to a running `MQTT` broker::

    asgimqtt --host localhost --port 1883 django_project.asgi:channel_layer


In your Django code::

    # routing.py
    channels_routing = [
        route("mqtt.sub", mqtt_consumer),
    ]

**Note**: you can only receive messages published in ``MQTT`` broker (channel
``mqtt.sub``).

The keys are:

* ``host``: host of the ``MQTT`` broker
* ``port``: port of the ``MQTT`` broker
* ``topic``: topic of the ``MQTT`` message
* ``payload``: payload of the ``MQTT`` message
* ``qos``: quality of service of the ``MQTT`` message (0, 1 or 2)
