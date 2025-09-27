from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

handler = SimpleHTTPRequestHandler

with HTTPServer(("", PORT), handler) as server:
    print(f"Server running on port {PORT}")
    server.serve_forever()

