from setuptools import setup
from asgimqtt import __version__

setup(
    name="asgimqtt",
    version=__version__,
    author="Emanuele Di Giacomo",
    author_email="emanuele.digiacomo@gmail.com",
    description="Interface between MQTT broker and ASGI",
    long_description=open("README.rst").read(),
    license="BSD",
    packages=["asgimqtt"],
    install_requires=[
        "paho-mqtt",
    ],
    entry_points={
        "console_scripts": [
            "asgimqtt=asgimqtt.cli:main",
        ]
    },
)
