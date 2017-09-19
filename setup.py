#!/usr/bin/python

from setuptools import setup

setup(
    name='tal-zipkin',
    version='0.1',
    url='https://github.com/TAKEALOT/tal-zipkin',
    description='Python wrappers to perform distributed tracing on services',
    install_requires=[
        'wsgiref',
        'pyramid',
        'requests',
        'pyramid_zipkin',
        'flask',
    ]
)
