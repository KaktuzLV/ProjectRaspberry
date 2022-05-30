from setuptools import setup

setup(
    name='sensor',
    version='0.1',
    description='Testing installation of Package Sensor',
    url='#',
    author='Silvestrs',
    author_email='psilvestrs@gmail.com',
    packages=['sensor', 'sensor.dht11'],
    zip_safe=False,
    install_requires=[
        #'Adafruit_DHT',
        'pysqlite3'
    ],
)


