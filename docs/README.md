# docs Directory

Welcome to the `docs` directory! This directory contains comprehensive notes on the OSI model layers and detailed specifications for practical exercises. Below is an overview of the contents in this directory.

## Table of Contents

- [docs Directory](#docs-directory)
  - [Table of Contents](#table-of-contents)
  - [Notes on OSI Model Layers](#notes-on-osi-model-layers)
    - [1 - Physical Layer](#1---physical-layer)
    - [2 - Data Link Layer](#2---data-link-layer)
    - [3 - Network Layer](#3---network-layer)
    - [4 - Transport Layer](#4---transport-layer)
    - [5 - Session Layer](#5---session-layer)
    - [6 - Presentation Layer](#6---presentation-layer)
    - [7 - Application Layer](#7---application-layer)
  - [Practicals Specifications](#practicals-specifications)

## Notes on OSI Model Layers

### 1 - Physical Layer

The Physical Layer is the first layer of the OSI model and is responsible for the physical connection between devices. It deals with the transmission and reception of raw bit streams over a physical medium such as cables, fiber optics, or wireless.

- **Functions**:
  - Bit-by-bit delivery
  - Modulation and demodulation
  - Signal transmission and reception
- **Components**:
  - Network cables
  - Hubs
  - Repeaters

### 2 - Data Link Layer

The Data Link Layer is responsible for node-to-node data transfer and error detection and correction. It ensures that data transferred between two nodes is error-free and properly synchronized.

- **Functions**:
  - Frame synchronization
  - Error detection and correction
  - Flow control
- **Components**:
  - Switches
  - Bridges
  - Network Interface Cards (NICs)

### 3 - Network Layer

The Network Layer is responsible for data routing, packet forwarding, and logical addressing. It determines the best path for data to travel from the source to the destination.

- **Functions**:
  - Logical addressing (IP addresses)
  - Routing
  - Packet forwarding
- **Components**:
  - Routers
  - Layer 3 switches

### 4 - Transport Layer

The Transport Layer ensures reliable data transfer between end systems. It provides services such as connection establishment, flow control, error recovery, and data segmentation.

- **Functions**:
  - Segmentation and reassembly
  - Connection control
  - Flow control
- **Protocols**:
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol)

### 5 - Session Layer

The Session Layer manages and controls the connections between applications. It establishes, maintains, and terminates sessions between two communicating hosts.

- **Functions**:
  - Session establishment, maintenance, and termination
  - Dialog control
  - Synchronization
- **Examples**:
  - Remote procedure calls (RPCs)
  - Session management protocols

### 6 - Presentation Layer

The Presentation Layer translates data between the application layer and the network format. It ensures that data is in a readable format for the application layer and can involve data encryption and compression.

- **Functions**:
  - Data translation
  - Data encryption and decryption
  - Data compression and decompression
- **Examples**:
  - Encryption protocols (SSL/TLS)
  - Character encoding (ASCII, EBCDIC)

### 7 - Application Layer

The Application Layer is the closest layer to the end user and interacts with software applications. It provides services for network applications such as email, file transfer, and web browsing.

- **Functions**:
  - Network process to application
  - Resource sharing
  - Remote file access
- **Protocols**:
  - HTTP/HTTPS
  - FTP
  - SMTP
- **YouTube Playlist**:
  - [NetworkProf](https://youtube.com/playlist?list=PLtjT6PTtgrGZCJMMQdti2AQa85P8LQIWy&feature=shared)
  - [Engineering Funda](https://www.youtube.com/watch?v=hOEj_0GFh2g&list=PLgwJf8NK-2e5utf4e5VJCEeNTDFtKHgsF)

## Practicals Specifications

The `Practicals.pdf` file contains detailed specifications for practical exercises related to each OSI model layer. These practicals are designed to provide hands-on experience and deepen understanding of the theoretical concepts.

- **Location**: `Practicals.pdf`
- **Content**:
  - Step-by-step instructions
  - Practical exercises for each OSI layer
  - Diagrams and examples
  - Evaluation criteria

Feel free to explore the notes and practicals to enhance your understanding of the OSI model and its applications in real-world networking scenarios. For any questions or further clarifications, please refer to the contact section in the main repository README file.
