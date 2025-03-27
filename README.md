# Computer Networks Project - ENEE2360

## Team Members
- **Sara Al-lahaleh** - ID: 1211083, Section 1
- **Malak Ammar** - ID: 1211470, Section 1
- **Asmaa Fares** - ID: 1210084, Section 3

## Instructor
- **Ibrahim Nemer**

## Date
- **06/05/2024**

---

## Project Overview

This project is a multifaceted exploration bridging networking concepts and web development. The goal of the project is to deepen the understanding of networking fundamentals while honing web development skills through practical implementation.

### Key Components:
1. **Network Analysis:**
   - Use of tools like Command Prompt, Wireshark, and nslookup for packet tracking, DNS message analysis, and network diagnostics.
   
2. **Socket Programming:**
   - Implementation of a peer-to-peer model using UDP, facilitating efficient communication between devices in the network.

3. **Web Server Development:**
   - Building a versatile web server capable of managing HTTP requests and serving diverse file types.
   - HTML and CSS-based pages are created to display project details and showcase the team members.

---

## Project Parts

### Part 1: Network Analysis and Tools

- **Ping**: Verifying network reachability.
- **Traceroute (tracert)**: Mapping the data route to a destination.
- **nslookup**: Resolving domain names to IP addresses.
- **Wireshark**: Capturing and analyzing DNS messages.
- **Tools Used**: Command Prompt, Wireshark, nslookup.

### Part 2: UDP Socket Programming for Peer-to-Peer Communication

- **UDP Communication**: Creation of a basic UDP-based messaging system for peer-to-peer communication.
- **Functionality**:
  - `get_ID()`: Computes subnet, host, and broadcast addresses.
  - `receive_message()` and `send_message()`: Listen for incoming messages and send outgoing messages, respectively.
  - Threaded architecture to manage send/receive operations on different devices.

### Part 3: Web Server Using Socket Programming

- **Objective**: Implementation of a versatile web server that handles HTTP requests and serves dynamic content.
- **Key Features**:
  - **GET and POST Request Handling**: Manage HTTP requests and serve HTML, CSS, and image files.
  - **Redirection**: Implement URL redirection for specific HTTP requests (e.g., `/so` for Stack Overflow).
  - **Error Handling**: Manage 404 errors and display user-friendly error pages.
  - **Server Setup**: Socket-based server listening on port 6060, capable of responding to various file requests and processing POST data.

### Web Pages

- **`main_en.html`**: English version of the landing page displaying team details.
- **`main_ar.html`**: Arabic version for users speaking Arabic.
- **`random.html`**: Page with a call-to-action for Palestine.
- **`myform.html`**: Form for users to request specific images from the server.

---

## Technologies Used

- **Python**: Main programming language for the socket-based server and request handling.
- **HTML/CSS**: Used for creating the web pages that are served by the web server.
- **Wireshark**: For network traffic analysis.
- **Command Prompt (CMD)**: For executing network diagnostic commands such as `ping`, `tracert`, `nslookup`.

---

## How to Run the Project

1. **Setup**:
   - Ensure Python 3.x is installed on your machine.
   - Download the necessary files: `main.py`, `main_en.html`, `style.css`, and other HTML files.

2. **Running the Web Server**:
   - Open a terminal or command prompt.
   - Navigate to the folder containing `main.py`.
   - Run the command:
     ```
     python main.py
     ```
   - The server will start listening on port 6060. Open a browser and go to `http://localhost:6060` to view the web pages.

3. **Test Communication (UDP)**:
   - To test the UDP communication, run the code on multiple devices or virtual machines connected to the same network. Each machine will listen and send messages using the `send_message()` and `receive_message()` functions.

---

## Conclusion

This project helped us better understand the core concepts of computer networks and socket programming while giving us hands-on experience in web server implementation. It combined both networking tools and web development, allowing us to explore practical aspects of data transmission and web communication.

---

## Contact

For any inquiries or issues regarding this project, feel free to contact the team via email:

- **Sara Al-lahaleh**: sara@example.com
- **Malak Ammar**: malak@example.com
- **Asmaa Fares**: asmaa@example.com
