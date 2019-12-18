# HTTPD Python Server

# Installation and usage 

```python
pip install pyserv
```
```bash
serv [port]
```

If no port is mentioned the server attempts to run on port 8080. If port 8080 is already in use the server attempts to bind to port 8081 and so on. If the server does not find any free port after 50 attempts the server stops.


