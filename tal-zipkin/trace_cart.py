import time
import os
import requests
from flask import Flask, request
from py_zipkin.zipkin import (ZipkinAttrs, create_http_headers_for_new_span,
                              zipkin_span)
from transport import http_transport
import tal_service_config

app = Flask(__name__)


@zipkin_span(service_name='cart-service', span_name='cart_service_do_stuff')
def cart_service_do_stuff():
    time.sleep(5)
    headers = create_http_headers_for_new_span()
    requests.get('http://www.kubernetes/cart', headers=headers)
    return 'OK'


@app.route('/')
def index():
    with zipkin_span(
        service_name='cart-service',
        span_name='index',
        transport_handler=http_transport,
        sample_rate=100,
        #0.05, # Value between 0.0 and 100.0
    ):
        cart_service_do_stuff()
        time.sleep(10)
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
