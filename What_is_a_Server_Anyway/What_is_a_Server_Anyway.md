---
options:
  end_slide_shorthand: true
  incremental_lists: true
---

# What is a Server Anyway?

## An introduction to Sockets, Networksw, and Servers in Python (or C if you're rad)

> A Presentation by: Nathan Laundry

---
# Who Am I?

- First year CS PhD student at UofT
- Founder and former president of the Computing Councils of Canada
- Advocate for Hacking (as in tinkering, not security)
- Unofficial el-presidente of the Toronto Computing Community
 (TCC)

> https://nathanlaundry.com 
> https://medium.com/@nathan.laundry
> https:TCC.com 

---
# Why am I Giving This Talk?
1. I wanted to teach myself something by teaching you something.
2. I wanted to Hack on something JUST for fun
3. I wanted to show you all that you don’t need to be an expert in something to deliver a presentation that’s useful and engaging to folks


---
# Why am I Giving This Talk?
## Also! Modern WebDev abstracts away so much it abstracts away fun


- `npm start` 
- `vercel deploy` 
- `railway up`

What does it do? What does it mean? Who cares? It's magic!

I don't know! Let's find out a little!

---

# Table of Contents

## Conceptual Overview

1. Sockets and IP: a story of Lonely Bob, Lazy me, and Socket-based Chats


## Coding Time

1. A Simple Server in Python (or C if you guys are rad)
2. A Simple Client in Python
3. HTTP and the Web

---

# Let's Begin

---

# The Situation

- Imagine it's the late 70s and there's no internet.
- Unix is sprouting up and folks are developing networking capabilities.
- I'm lazy and I want to chat with my friend Bob who's in the next room over without getting up.

I've got a computer, Bob's got a computer. It's time to get these things talking.

---

# Cue SOCKETS

Sockets allow two-way communication between computers over a network.

Sockets take on two roles depending on if they're running on the client or the server:
- **Server Socket**: Listens for incoming connections
- **Client Socket**: Initiates a connection to the server

Once they're connected, they can send and receive data from one another over the network.

---

## Setting Up Your Connection

To send a message to Bob, we'll use those two sockets: 
- Bob's machine is going to be the server - Listening
- My machine is going to be the client - Connecting

---

## Bob Sets Up a Listening Socket

Bob sets up his UNIX machine to run a program that creates a server socket.

This server socket LISTENS for incoming connections on a PORT

### Hold on - What's a Port?

- The server may have many different sockets open and listening. 
- Somehow it has to know which one to send the connection to. 
- Imagine the server is like an apartment building. 
- The PORTs are like the mailboxes in the lobby. 
- Each mailbox has an address for a specific apartment. 
- Just like each PORT has an address for a specific program.

---

## I Create a Socket to Connect to Bob's Listening Socket

To do this, we have two tasks:

1. figure out what Bob's IP address is
2. ask Bob what port he's running his listening socket on
3. setup a socket on our machine
4. get that socket to initiate a connection to Bob's machine

### What's an IP Address?

> An IP address is like a street address or a ZIP/Postal Code 
> If a PORT is the mailbox in the lobby
> the IP address is the building's address

--- 

## Creating the Client Socket and the Handshake

- we write a small program that sets up a client socket
- we tell the client socket "Hey, Bob's IP address is X and he's listening on port Y"
    - the IP probably looks like: 192.168.1.XXX
    - the PORT is gonna be something like 8080
- The client socket, with the IP and port known, then goes "Hey Bob, I want to talk to you" and Bob's server socket goes "Hey, I'm so bored, let's talk."
- This is called the handshake

---

## Sending the Message

Now that a direct line (connection) is established between your client socket and Bob's server socket, you can send your message.

- **You:** Your client socket sends a stream of data (your message) through the connection.
- **Bob's Machine:** Bob's server socket receives the incoming data, and Bob's program reads it and displays it on his screen.

---

## Bob Replies

If Bob wants to reply, his server program can send a message back through the same connection to your client program, which you can then read on your terminal.
- Remeber this is a two-way connection!

---

## Closing the Connection

Once your chat is over, either side can "hang up" by closing their socket, neatly ending the conversation and freeing up the system resources.

---

# Coding Time

Okay, so we now we generally know how this works.
Let's build it.

---

# A simple server in Python

The following code does:
- creates a socket
- binds the socket to the IP address gotten by "gethostname" and the port 9999
- It then listens for a connection, accepts it, thanks the client, and closes the connection

Is it useful? No. Is it fun. I think so.

---
# A simple Server in Python
```python
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

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    msg = 'Thank you for connecting'+ "\r\n"
    client_socket.send(msg.encode('ascii'))
    client_socket.close()
```
---

# A simple client in Python

This code does the following:
- creates a socket
- sets the host and port (we're going to connect to a socket on our own machine here)
- requests a connection
- upon accept, receives a message of no more than 1kb
- closes the connection
---

# A simple client in Python
```python
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Connection to hostname on the port.
client_socket.connect((host, port))

# Receive no more than 1024 bytes
msg = client_socket.recv(1024)

client_socket.close()
print(msg.decode('ascii'))

```

---

# Chatting with Sockets


To add chat in, we just have to make use of:
- socket.send
- socket.recv

--- 
# Chatting with Sockets
## Server Time
```python
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
# Note how we store the client_socket and use it later to send and recieve messages
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
```

---
# Chatting with Sockets
## Client Time

```python
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
```

---

# What does this have to do with HTTP Servers??

> It's the same thing ... More or less.

There's a bunch of stuff about HTTP (HyperText Transfer Protocol) that I wont' get into BUUUUT

With an HTTP server, we respond with formatted text like:
- Hyper Text Markup Language (HTML)
- JSON Javascript object notation

Let's see that in action

---

# Updating our Server to Respond with HTML 

Remember our our original simple server?

```python
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

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    msg = 'Thank you for connecting'+ "\r\n"
    client_socket.send(msg.encode('ascii'))
    client_socket.close()
```

We're just going to update this so that instead of responding with an ASCII message we respond with an http_response containing HTML

---
# Now With new shiny HTML response!!

```python
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

```

---

# There you go

A simple HTTP server from start to finish in python

I hope you had fun
