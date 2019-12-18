#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info(f"{bcolors.OKBLUE}GET {bcolors.ENDC} request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info(f"{bcolors.OKGREEN}POST {bcolors.ENDC} request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    
    for i in range(50):
        try :
            server_address = ('', port)
            httpd = server_class(server_address, handler_class)
            break
        except OSError:
            port += 1
            logging.info(f"{bcolors.WARNING}PORT " + str(port-1) + " is unavalible. Trying PORT " + str(port) + f"{bcolors.ENDC}")
    
    logging.info(f'{bcolors.OKGREEN}Starting HTTP SERVER at PORT ' + str(port) + f'{bcolors.ENDC}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


        logging.info(f'port '+str(port-1)+' is taken. Trying port ' + str(port))
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
