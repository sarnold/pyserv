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

### GET and POST request example

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

INFO:root:GET  request,
Path: /
Headers:
Host: 0.0.0.0:8080
User-Agent: python-requests/2.21.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive



127.0.0.1 - - [18/Dec/2019 18:01:52] "GET / HTTP/1.1" 200 -

```


#### POST request to the server

```python

>>> import requests
>>> URL = 'http://0.0.0.0:8080'
>>> r = requests.post(URL)
>>> print(r.text)
POST request for /

```
On the server side you will get 

```bash
INFO:root:POST  request,
Path: /
Headers:
Host: 0.0.0.0:8080
User-Agent: python-requests/2.21.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Length: 0



Body:


127.0.0.1 - - [18/Dec/2019 18:03:07] "POST / HTTP/1.1" 200 -

```
If no port is mentioned the server attempts to run on port 8080. 

If the given port (or the default port 8080) is already in use the server attempts to bind the next port. If the server does not find any free port after 50 attempts the server stops.


