#Malak Ammar 1211470
#Asmaa Fares 1210084
#Sarah Adnan 1211083

from socket import *
import os

def parse_request(sentence):
    # Parse the HTTP request to extract relevant information
    x = sentence.split("\n")
    y = x[0].split("/")
    z = y[1].split(" ")
    r = z[0].split(".")
    return z, r

def send_response(connectionSocket, status, content_type, content):
    # Send HTTP response headers to the client
    connectionSocket.send(f"HTTP/1.1 {status}\r\n".encode())
    connectionSocket.send(f"Content-Type: {content_type}\r\n".encode())
    connectionSocket.send("\r\n".encode())

    # Send the content of the response
    if isinstance(content, str):
        connectionSocket.send(content.encode())
    else:
        connectionSocket.send(content)

def handle_request(connectionSocket, addr, sentence):
    # Print the HTTP request in the terminal
    print("Received HTTP request:")
    print(sentence)

    ip = addr[0]
    port = addr[1]

    z, r = parse_request(sentence)

    # Define a dictionary mapping file extensions to content types
    content_types = {
        "html": "text/html",
        "css": "text/css",
        "png": "image/png",
        "jpg": "image/jpeg",
    }

    # Handle POST requests
    if sentence.startswith("POST"):
        # Extract image name from the POST data
        image_name = sentence.split('\r\n')[-1].split('=')[-1]
        image_path = f'images/{image_name}'

        # Check if the image exists
        if os.path.isfile(image_path):
            # Read the image content
            with open(image_path, "rb") as f:
                content = f.read()

            # Send the image as response
            send_response(connectionSocket, "200 OK", "image/png", content)
        else:
            # Handle requests for unknown images
            with open("error.html", "r") as f:
                content = f.read()
            send_response(connectionSocket, "404 Not Found", "text/html", content)
        return

    # Handle requests for specific files or paths
    if z[0] in ["", "main_en.html", "index.html", "en"]:
        file_path = "main_en.html"
    elif z[0] == "ar":
        file_path = "main_ar.html"
    else:
        file_path = z[0]

    # Handle requests for redirection
    if r[-1] == "so" and len(r) == 1:
        connectionSocket.send(b"HTTP/1.1 307 Temporary Redirect\r\n")
        connectionSocket.send(b"Content-Type: text/html\r\n")
        connectionSocket.send(b"Location: https://stackoverflow.com/\r\n")
        connectionSocket.send(b"\r\n")
        return
    elif r[-1] == "itc" and len(r) == 1:
        connectionSocket.send(b"HTTP/1.1 307 Temporary Redirect\r\n")
        connectionSocket.send(b"Content-Type: text/html\r\n")
        connectionSocket.send(b"Location: https://itc.birzeit.edu/login/index.php\r\n")
        connectionSocket.send(b"\r\n")
        return

    # Check if the requested file exists
    if os.path.isfile(file_path):
        # Get the file extension
        file_extension = file_path.split(".")[-1]

        # Get the content type from the dictionary
        content_type = content_types.get(file_extension, "text/plain")

        # Read the content of the file
        with open(file_path, "rb") as f:
            content = f.read()

        # Send the response
        send_response(connectionSocket, "200 OK", content_type, content)
    else:
        # Handle requests for unknown files or paths
        with open("error.html", "r") as f:
            content = f.read()
        send_response(connectionSocket, "404 Not Found", "text/html", content)

def start_server():
    serverPort = 6060
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("THE SERVER IS READY TO RECEIVE")

    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        handle_request(connectionSocket, addr, sentence)
        connectionSocket.close()

if __name__ == "__main__":
    start_server()
