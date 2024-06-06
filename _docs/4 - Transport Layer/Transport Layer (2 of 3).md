# Reliable Communication (Transport Layer)

## Definition
Reliable communication refers to the guarantee that data sent from one end of a network to another will arrive intact and in order, without loss or duplication.

## Role of the Transport Layer
The Transport Layer is responsible for providing reliable, end-to-end communication services for applications. It uses various mechanisms to ensure the reliability of data transmission.

## Key Concepts
1. **Error Detection and Correction:** The Transport Layer uses checksums to detect errors in data. If an error is detected, the data can be retransmitted.
2. **Sequencing:** The Transport Layer adds sequence numbers to data packets to ensure they are reassembled in the correct order at the destination.
3. **Acknowledgements and Retransmissions:** The receiver sends an acknowledgement packet back to the sender for each packet it receives. If the sender does not receive an acknowledgement within a certain time frame, it assumes the packet was lost and retransmits it.
4. **Flow Control:** The Transport Layer manages the rate of data transmission to prevent a fast sender from overwhelming a slow receiver.

## TCP and Reliable Communication
TCP (Transmission Control Protocol) is a key protocol used at the Transport Layer that provides reliable communication. It uses the mechanisms mentioned above to ensure data is correctly transmitted from the source to the destination.

#### Key Insights

- Automatic repeat request (ARQ) is a mechanism used to ensure reliability in the transport layer. It involves numbering packets, acknowledging them, and retransmitting if necessary. ARQ helps minimize data loss caused by factors like packet loss or recipient unavailability.
- TCP uses sequence numbers for packets, allowing for reliable data communication. The sender keeps track of the next sequence number to send, while the receiver acknowledges the packets it has received. This helps ensure data integrity and order.
- UDP, on the other hand, lacks reliability mechanisms like sequence numbers and acknowledgments. It does not guarantee data delivery or ordering, making it suitable for applications where speed is prioritized over reliability.
- In ARQ, various events can occur, such as receiving a packet, sending a packet, receiving a negative acknowledgement, retransmit timer expiration, and acknowledgement timer expiration. These events trigger actions like retransmitting packets or acknowledging received packets.
- TCP handles flow control using window advertisement. The sender includes information about its available window space in each message, allowing the receiver to know how much data it can receive. This helps prevent overwhelming the recipient's buffer.
- Buffer size and window advertisement can change dynamically based on data consumption and communication between sender and receiver. This ensures efficient utilization of resources and adaptability to varying network conditions.
- Understanding the concepts of reliability, ARQ, and flow control is crucial for building robust and efficient communication protocols in computer networks. These mechanisms help ensure data integrity, minimize losses, and optimize network performance.