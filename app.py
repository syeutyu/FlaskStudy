import http.server
import socketserver

PORT = 8081

Handler = http.server.CGIHTTPRequestHandler

httpd = socketserver.TCPServer(("",PORT), Handler)

httpd.server_name = "localhost"
httpd.server_port = PORT
print("Start Server")

httpd.serve_forever()