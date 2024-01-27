"""
SaberStat Server: Dispaying Hits/Misses
"""
import http.server
import socketserver
import http.client
import json
import logging
import pandas as pd

PORT = 8000
FRONTEND_HOST = 'localhost'
FRONTEND_PORT = 5500

class Server(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Forward the POST request to the frontend
        frontend_conn = http.client.HTTPConnection(f'{FRONTEND_HOST}:{FRONTEND_PORT}')
        headers = {'Content-type': 'application/json'}
        frontend_conn.request('POST', '/', body=post_data, headers=headers)
        response = frontend_conn.getresponse()

        logging.info("POST request forwarded to frontend,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        # Send the same response back to the client
        self._set_response()
        self.wfile.write(response.read())

def run(server_class=http.server.HTTPServer, handler_class=Server, port=PORT):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd on port %s...\n', port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == "__main__":
    run()
