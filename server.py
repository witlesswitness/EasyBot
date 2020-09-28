#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import time
import logging

# print('readfileserver.py')

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        pathnew = ''
        pathnew = self.path
        # print(pathnew)
        newpath = ''
        newpath = ('/home/kali/project/webserver/logs'+pathnew)
        # print(newpath)
        if pathnew == '/favicon.ico':
            pass
        else:
            with open(newpath) as input_file:
                contents = input_file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>https://botsassemble.com</title></head>", "utf-8"))
                # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                # self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes(contents, "utf-8"))
                # self.wfile.write(bytes("</body></html>", "utf-8"))

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

if __name__ == "__main__":   
    # print('readfileserver.py/main')     
    webServer = HTTPServer((hostName, serverPort), MyServer)
    logging.basicConfig(filename=('/home/kali/project/webserver/logs/logs.txt'), format='%(message)s', level=logging.INFO)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
