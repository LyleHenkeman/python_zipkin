from flask import Flask, request

app = Flask(__name__)


from py_zipkin.zipkin import zipkin_span, ZipkinAttrs

import requests
import time
from transport import http_transport


@zipkin_span(service_name='service1', span_name='service1_do_stuff')
def cart_service_do_stuff():
    time.sleep(5)
    return 'OK'


@app.route('/cart-service/')
def index():
    with zipkin_span(
        service_name='cart-service',
        zipkin_attrs=ZipkinAttrs(
            trace_id=request.headers['X-B3-TraceID'],
            span_id=request.headers['X-B3-SpanID'],
            parent_span_id=request.headers['X-B3-ParentSpanID'],
            flags=request.headers['X-B3-Flags'],
            is_sampled=request.headers['X-B3-Sampled'],
        ),
        span_name='index_cart_service',
        transport_handler=http_transport,
        sample_rate=100,
        #0.05, # Value between 0.0 and 100.0
    ):
        cart_service_do_stuff()
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=1234, debug=True)
