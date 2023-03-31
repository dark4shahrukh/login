import http.server
import ssl

port= 443
directory = '.'
httpd = http.server.HTTPServer(('localhost',port),http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./certfile.crt',keyfile='./keyfile.key', server_side=True)

print('Starting server')
httpd.serve_forever()

