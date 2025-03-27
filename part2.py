#Malak Ammar 1211470
#Asmaa Fares 1210084
#Sarah Adnan 1211083

import socket
import threading
import datetime

# Peer details
PEER_FIRST_NAME = input("Enter your first name: ")
PEER_LAST_NAME = input("Enter your last name: ")

# IP and MASK details
IP = '192.168.88.13'
MASK = '255.255.255.0'


def get_ID(ip, mask):
    ip = ip.split('.')
    mask = mask.split('.')
    ip = [int(octet) for octet in ip]
    mask = [int(octet) for octet in mask]
    subnet = [str(ip_octet & mask_octet) for ip_octet, mask_octet in zip(ip, mask)]
    host = [str(ip_octet & ~mask_octet) for ip_octet, mask_octet in zip(ip, mask)]
    broadcast = [str(ip_octet | ~mask_octet & 0xFF) for ip_octet, mask_octet in zip(ip, mask)]
    subnet_mask = '.'.join(subnet)
    print('Subnet: {0}'.format(subnet_mask))
    print('Host: {0}'.format('.'.join(host)))
    print('Broadcast address: {0}'.format('.'.join(broadcast)))
    return subnet_mask


def receive_message():
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_instance.bind(('', SERVER_PORT))

    while not exit_flag:
        try:
            data, _ = socket_instance.recvfrom(BUFFER_SIZE)
            message = data.decode()
            sender_ip, sender_first_name, sender_last_name, message_content = message.split('|')
            print(f"Received a message from {sender_first_name} {sender_last_name} at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Message Content: {message_content}")
            # Update last received message from sender
            last_received_messages[sender_ip] = (sender_first_name, sender_last_name, datetime.datetime.now())

            # Check if you are the receiver
            if sender_ip == IP:
                print("You are the receiver.")


        except socket.timeout:
            continue
        except KeyboardInterrupt:
            break



def send_message():

    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_instance.bind(('', 0))  # Bind to any available port on this machine

    while not exit_flag:
        message_content = input("\nEnter your message: \n")
        message = f"{socket.gethostbyname(socket.gethostname())}|{PEER_FIRST_NAME}|{PEER_LAST_NAME}|{message_content}"
        broadcast_address = "192.168.88.255"
        try:
            socket_instance.sendto(message.encode(), (broadcast_address, SERVER_PORT))
        except PermissionError:
            print("Permission denied. Make sure to run the script with appropriate permissions.")
            break


# Create a UDP socket


# Display IP and MASK details
subnet_mask = get_ID(IP, MASK)
print("Subnet Mask:", subnet_mask)

# Server details
SERVER_PORT = 5051
BUFFER_SIZE = 1024

# Dictionary to store the last received message from each peer
last_received_messages = {}

# Flag to indicate when to exit the threads
exit_flag = False

# Start receiving messages in a separate thread if the role is receiver

receive_thread = threading.Thread(target=receive_message, args=())
receive_thread.start()

# Start sending messages in a separate thread if the role is sender

send_thread = threading.Thread(target=send_message, args=())
send_thread.start()

send_thread.join()
receive_thread.join()
# Display the last received message from each peer
print("\nLast received messages from other peers:")
for ip, (first_name, last_name, timestamp) in last_received_messages.items():
    print(f"Received a message from {first_name} {last_name} at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")