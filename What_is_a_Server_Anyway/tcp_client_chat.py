import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Connect to the server on the port
client_socket.connect((host, port))

try:
    while True:
        message = input("You: ")
        client_socket.send(message.encode('ascii'))
        if message == 'bye':
            break
        # Wait for response from the server
        response = client_socket.recv(1024).decode('ascii')
        print(f"Server: {response}")
finally:
    client_socket.close()

