import http.server
import socketserver
import logging
import json
import pandas as pd
import matplotlib.pyplot as plt

PORT = 8000

class Server(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()
        
        # Save the JSON data to the log file
        with open("log.json", "a") as f:
            f.write(post_data.decode('utf-8'))
            f.write(",\n")

def plot_data():
    # Read the JSON file into a Pandas DataFrame
    try:
        df = pd.read_json("log.json", lines=True)
        
        # Extract the relevant data for plotting (change 'rotationRateX' to your desired column)
        column_to_plot = 'rotationRateX'
        values_to_plot = df['payload'].apply(lambda x: x[0]['values'][column_to_plot] if x else None)
        
        # Plot the data
        plt.plot(values_to_plot, label=column_to_plot)
        plt.xlabel('Index')
        plt.ylabel(column_to_plot)
        plt.legend()
        plt.title(f'Plot of {column_to_plot}')
        plt.show()

    except pd.errors.EmptyDataError:
        print("No data to plot.")

def run(server_class=http.server.HTTPServer, handler_class=Server, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        logging.info('Stopping httpd...\n')
    
    # Plot the data after the server has finished serving requests or after Ctrl+C
    plot_data()

if __name__ == "__main__":
    run()
