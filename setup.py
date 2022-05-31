import setuptools
from setuptools import setup

setup(
    name='sensor',
    version='0.1',
    description='Testing installation of Package Sensor',
    url='#',
    author='Silvestrs',
    author_email='psilvestrs@gmail.com',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    zip_safe=False,
    install_requires=[
        'Adafruit_DHT',
        'pysqlite3'
    ],
    entry_points={
        'console_scripts': [
            # 'vriRandom=src.sensor.main:testCmd',
            # 'runMainPy=src.sensor.main:runMain'
        ]
    }
)
