from http.server import HTTPServer, BaseHTTPRequestHandler
import os
port = int(os.environ.get('PORT', '80'))
customer_name = os.environ.get('CUSTOMER_NAME', 'None')
class HelloHandler(BaseHTTPRequestHandler): 
    def do_GET(self):
        if self.path == "/welcome":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(f"Hello {customer_name}", "utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Wrong url", "utf-8"))
server = HTTPServer(('', port), HelloHandler)
server.serve_forever()