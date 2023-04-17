import math
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the port number
PORT_NUMBER = 5000

# Create a class that handles HTTP requests
class MyHandler(BaseHTTPRequestHandler):
    
    # Define a method to handle GET requests
    def do_GET(self):
        try:
            # Get the integer value from the URL path
            n = int(self.path[1:])

            # Calculate the square root of n
            result = math.sqrt(n)

            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(str(result), "utf-8"))

        except ValueError:
            # Send an error response if the URL path does not contain a valid integer
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Invalid input: please enter a valid integer in the URL path", "utf-8"))

# Create a server instance and start listening on the defined port
if __name__ == '__main__':
    try:
        server = HTTPServer(('', PORT_NUMBER), MyHandler)
        print('Started httpserver on port', PORT_NUMBER)
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()
