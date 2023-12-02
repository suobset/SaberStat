"""
SaberStat Server: Dispaying Hits/Misses
"""
import tkinter as tk
import statInterface
import http.server
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        print("Received POST request data:")
        print(post_data)

        self._set_response()
        self.wfile.write("Data received successfully!\n".encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server stopped.')

if __name__ == "__main__":
    root = tk.Tk()
    app = statInterface.SaberStatUI(root)
    #root.mainloop()
    ###
    run_server()