# Process-to-Process (Transport Layer)

## Definition
Process-to-process communication refers to the exchange of data between two processes running on different systems. In the context of the Transport Layer, it involves establishing a virtual communication path between these processes and ensuring that data is reliably transmitted.

## Role of the Transport Layer
The Transport Layer is responsible for providing reliable, process-to-process communication services for applications. It provides mechanisms for the establishment, maintenance, and termination of virtual circuits, transport fault detection and recovery, and information flow control.

## Key Concepts
1. **Port Numbers:** Each process running on a system is assigned a unique port number. The Transport Layer uses these port numbers to identify the source and destination processes for each packet of data.
2. **TCP and UDP:** TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are the two main protocols used at the Transport Layer. TCP provides reliable, connection-oriented communication, while UDP provides faster, connectionless communication.
3. **Flow Control:** The Transport Layer manages the rate of data transmission between two nodes to prevent a fast sender from overwhelming a slow receiver.
4. **Error Control:** The Transport Layer handles error checking and recovery. If a packet is lost or corrupted, the Transport Layer can request that it be retransmitted.

## Process-to-Process Communication and the Transport Layer
The Transport Layer provides the necessary services for process-to-process communication. It ensures that data is correctly transmitted from the source process to the destination process, managing issues like data flow, error control, and multiplexing.

#### Key Insights

- The Transport layer provides a reliable connection between processes, ensuring that communication happens and that parties are aware of any failures. This reliability is crucial for applications such as financial transactions.
- TCP and UDP are two primary examples of transport layer protocols. TCP is connection-oriented, meaning that a connection is established before communication, while UDP is connectionless, relying on packets being sent without prior setup.
- The three-way handshake is used in TCP to establish and terminate connections. It involves the exchange of SYN and ACK messages between the communicating parties, ensuring that both parties are aware and willing to communicate.
- The Transport layer plays a critical role in the OSI protocol stack, serving as a bridge between the application-oriented upper layers and the network-oriented lower layers. It allows applications to communicate without having to worry about the underlying network infrastructure.
- The choice between connection-oriented and connectionless approaches in the Transport layer depends on the specific needs of the application and the infrastructure available. Connection-oriented protocols offer greater reliability but may come at a higher cost, while connectionless protocols may be more suitable for certain types of data transmission, such as video streaming.
