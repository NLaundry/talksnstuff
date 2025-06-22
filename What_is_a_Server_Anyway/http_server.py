import socket

def handle_request(client_socket):
    """Reads the request and sends a basic HTTP response"""
    request = client_socket.recv(1024)
    print(f"Received request: {request.decode('utf-8')}")

    http_response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Server Response</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a simple HTTP server response with some extra HTML.</p>
        <ul>
            <li>HTML item 1</li>
            <li>HTML item 2</li>
            <li>HTML item 3</li>
        </ul>
    </body>
    </html>
    """

    client_socket.sendall(http_response.encode('ascii'))

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and set port
host = 'localhost'
port = 9999

# Bind to the port and start listening
server_socket.bind((host, port))
server_socket.listen(5)

print("Serving HTTP on port %s ..." % port)

while True:
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    handle_request(client_socket)
    client_socket.close()

