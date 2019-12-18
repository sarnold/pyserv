# HTTPD Python Server

# Installation and usage 

```python
pip install pyserv
```
```bash
serv [port]
```

# Examples :

```bash
serv 8080
```
The output would be 
```bash
...
INFO:root:Starting HTTP SERVER at PORT 8080
```

## GET and POST request example

```
>>> import requests
>>> URL = 'http://0.0.0.0:8080'
>>> r = requests.get(URL)
>>> print(r.text)
GET request for /
```

If no port is mentioned the server attempts to run on port 8080. 

If the given port (or the default port 8080) is already in use the server attempts to bind the next port. If the server does not find any free port after 50 attempts the server stops.


