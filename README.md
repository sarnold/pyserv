# HTTPD Python Server

## Installation and usage 

```python
pip install pyserv
```
```bash
serv [port]
```

## Examples :

```bash
serv 8080
```
The output would be 
```bash
...
INFO:root:Starting HTTP SERVER at PORT 8080
```

### GET request example

Open a new terminal and try out sending GET and POST requests

```python
$ python
>>> import requests
>>> URL = 'http://0.0.0.0:8080'
>>> r = requests.get(URL)
>>> print(r.text)
GET request for /
```
On the server side you would get

```bash

INFO:root:Path: /
INFO:root:Headers:
Host: 0.0.0.0:8080
User-Agent: python-requests/2.25.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive



127.0.0.1 - - [24/Jun/2022 21:23:07] "GET / HTTP/1.1" 200 -

```

If no port is mentioned the server attempts to run on port 8080. 

If the given port (or the default port 8080) is already in use, you will
need to pass a different port number, eg, 8088.

Motivation:

https://pypi.org/project/pyserv/

https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
