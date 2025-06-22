import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Bind to the port
server_socket.bind((host, port))

# Queue up to 5 requests
server_socket.listen(5)

print("Server waiting for connection...")
client_socket, addr = server_socket.accept()
print(f"Got a connection from {addr}")

try:
    while True:
        # Receive message from the client
        msg = client_socket.recv(1024).decode('ascii')
        if msg == 'bye':
            break
        print(f"Client: {msg}")
        response = input("Reply: ")
        client_socket.send(response.encode('ascii'))
finally:
    client_socket.close()
    server_socket.close()

