# Computer Networking: Network Protocols Implementation

<img src="images/readme.jpg" style="width: 100%; height: 40%;" />

A comprehensive collection of network protocol implementations and server applications built from scratch to demonstrate core networking concepts and server-side programming.

## Overview

This repository contains a collection of projects focusing on different server and client implementations, including CGI scripts, FTP, LDAP, POP3, SMTP servers, and more. Below is an overview of each project contained in this repository.

## Components

**CGI Script on the Web** - (`src/cgi-web-demo`)
- Demonstrates how to deploy CGI scripts on the web, including examples and guidelines for generating dynamic web content.  
- Basic CGI script examples  
- Deployment instructions  
- Security best practices  
- **Languages:** Python, Perl  

**CGI Scripts** - (`src/cgi-scripts`)
- A collection of CGI scripts for handling form data and generating dynamic web content.  
- Multiple script examples  
- Form handling  
- Data processing  
- **Languages:** Python, Perl  

**FTP Server** - (`src/ftp-server`)
- Implementation of an FTP server supporting file transfers, user authentication, and configuration.  
- FTP protocol implementation  
- User authentication  
- File upload/download  
- **Languages:** Python  

**LDAP Client** - (`src/ldap-client`)
- LDAP client implementation for connecting to LDAP servers, performing searches, and retrieving directory information.  
- LDAP server connection  
- Search and retrieval operations  
- Example usage scripts  
- **Languages:** Python  

**POP3 Client+Proxy** - (`src/pop3-client-proxy`)
- Combined POP3 client and proxy server for connecting to POP3 email servers and relaying email traffic.  
- POP3 protocol implementation  
- Proxy functionality  
- Email retrieval and forwarding  
- **Languages:** Python  

**POP3 Server** - (`src/pop3-server`)
- POP3 server implementation allowing clients to connect and retrieve emails.  
- POP3 protocol support  
- User authentication  
- Email storage and retrieval  
- **Languages:** Python  

**Quiz Server** - (`src/quiz-server`)
- Server application for hosting quizzes, enabling user interaction and scoring.  
- Quiz hosting  
- User interaction  
- Scoring system  
- **Languages:** Python  

**Quiz Web Server** - (`src/quiz-web-server`)
- Web-based quiz server presenting quizzes through a web interface with real-time scoring.  
- Web-based interface  
- Interactive quizzes  
- Real-time scoring  
- **Languages:** Python, HTML, JavaScript  

**SMTP Server** - (`src/smtp-server`)
- SMTP server implementation for sending and receiving email messages.  
- SMTP protocol support  
- Email sending/receiving  
- User authentication 
- **Languages:** Python  

## Notes

The `docs` folder contains detailed summaies for each layer in the OSI ISO Reference Model, It also contains the specification for these projects, basically the practical specification.

- **Location**: `docs/`

## Protocol Coverage

- HTTP/1.1 with CGI support
- FTP with active/passive modes
- SMTP for email transmission
- POP3 for email retrieval
- LDAP for directory services
- Telnet for remote terminal access
- PROXY for the POP3 client

## Security Notice

These implementations are designed for educational purposes and protocol understanding. They may not include production-level security features.

## Credits

- [NetworkProf](https://youtube.com/playlist?list=PLtjT6PTtgrGZCJMMQdti2AQa85P8LQIWy&feature=shared)
- [Engineering Funda](https://www.youtube.com/watch?v=hOEj_0GFh2g&list=PLgwJf8NK-2e5utf4e5VJCEeNTDFtKHgsF)
- [Feduguide](https://eduguide.co.in/what-are-the-4-main-types-of-computer-networks)

Feel free to explore the notes and practicals to enhance your understanding of the OSI model and its applications in real-world networking scenarios. For any questions or further clarifications, please refer to the contact section in the main repository README file.

---

---