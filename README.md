# HTTPD Python Server

# Installation and usage 

```python
pip install pyserv
```
```bash
serv [port]
```

Example :

If no port is mentioned the server attempts to run on port 8080. 

If the given port (or the default port 8080) is already in use the server attempts to bind the next port. If the server does not find any free port after 50 attempts the server stops.


