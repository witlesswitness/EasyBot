#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import time
import logging
import os
import editbotname

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        pathnew = ''
        pathnew = self.path
        newpath = ''
        newpath = ('./server/'+pathnew)
        if pathnew == '/favicon.ico':
            pass
        else:
            with open(newpath) as input_file:
                contents = input_file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(contents, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        logging.info("\nPath: %s      Body:%s",
                str(self.path), body.decode('utf-8'))
        self.end_headers()
        response = BytesIO()
        response.write(b'This is a POST request. ')
        response.write(b'Received: ')
        response.write(body + b'\n')
        self.wfile.write(response.getvalue())
        editbotname.main()
def directoryhandler():
    dir = os.path.join('./','server')
    if not os.path.exists(dir):
        os.mkdir(dir)
        os.chdir(dir)
        f = open('botnames.txt', 'w+')
        f.write('0')
        f.close()
        f = open('instructions.txt', 'w+')
        f.write('')
        f.close()
        f = open('logs.txt', 'w+')
        f.write('')
        f.close()
if __name__ == "__main__":
    directoryhandler()
    webServer = HTTPServer((hostName, serverPort), MyServer)
    logging.basicConfig(filename=('./server/logs.txt'), format='%(message)s', level=logging.INFO)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
