# tal-zipkin
[Zipkin](http://zipkin.io) is a distributed tracing system. It helps gather timing data needed to troubleshoot latency problems in microservice architectures. It manages both the collection and lookup of this data. Zipkin’s design is based on the [Google Dapper paper](http://research.google.com/pubs/pub36356.html). Zipkin allows you to see the how long the whole operation took, as well how much time was spent in each service.

This project includes a dependency-free library and a [spring-boot](http://projects.spring.io/spring-boot/) server. Storage options include in-memory, JDBC (mysql), Cassandra, and Elasticsearch. This repo are the Python wrappers we can use to trace Takealot services.

## Quick-start

The quickest way to get started is to fetch the [latest released server](https://search.maven.org/remote_content?g=io.zipkin.java&a=zipkin-server&v=LATEST&c=exec) as a self-contained executable jar. Note that the Zipkin server requires minimum JRE 8.

# Implementation Overview

Web requests are served by [Pyramid](http://www.pylonsproject.org/) routes, and tracing is automatically performed for you by [pyramid_zipkin](https://github.com/Yelp/pyramid_zipkin).

## Setup

Before you start anything, you'll need to download the libraries:
```bash
$ python setup.py install
```

Start zipkin as a Docker container.
```bash
docker-compose up
```
