import os.path
import re
from setuptools import setup


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="asgimqtt",
    version=get_version("asgimqtt"),
    author="Emanuele Di Giacomo",
    author_email="emanuele@digiacomo.cc",
    url="https://github.com/edigiacomo/asgi-mqtt",
    description="Interface between MQTT broker and ASGI",
    long_description=open("README.rst").read(),
    license="GPLv2+",
    packages=["asgimqtt"],
    install_requires=[
        "paho-mqtt",
    ],
    entry_points={
        "console_scripts": [
            "asgimqtt=asgimqtt.cli:main",
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
