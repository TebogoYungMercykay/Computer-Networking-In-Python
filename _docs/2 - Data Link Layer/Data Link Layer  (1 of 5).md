# Themes and Error Control (Data Link Layer)

## Themes in the Data Link Layer
1. **Framing:** The Data Link Layer takes packets from the Network Layer and encapsulates them into frames for transmission.
2. **Physical Addressing:** The Data Link Layer adds a header to the frame to define the physical address of the sender or receiver of the frame.
3. **Flow Control:** If the rate at which data is taken by the receiver is less than the rate produced in the sender, then the Data Link Layer imposes a flow control mechanism to prevent overwhelming the receiver.
4. **Error Control:** The Data Link Layer adds reliability to the Physical Layer by adding mechanisms to detect and retransmit damaged or lost frames. Also, it uses a mechanism to recognize duplicate frames. Error control is normally achieved through a trailer added to the end of the frame.

## Error Control
Error control is a critical aspect of the Data Link Layer. It ensures that frames are transmitted with no errors. Error control is both error detection and error correction. It allows the receiver to inform the sender of any frames that were lost or damaged and coordinates the retransmission of those frames by the sender.

1. **Error Detection:** Techniques such as parity check, checksum, and cyclic redundancy check (CRC) are used to detect errors in the transmitted data.
2. **Error Correction:** Techniques such as Hamming code are used to correct errors without needing retransmission.

The Data Link Layer plays a crucial role in providing a reliable communication link between two directly connected nodes.

#### Key Insights

- The use of master/slave setups for managing link control in mainframes and terminals allowed efficient information exchange.
- Multi-point links enabled connection of multiple terminals to a single link, with only the addressed terminal responding, improving network efficiency.
- Managing the link between two equal mainframes posed challenges in determining control, leading to the need for alternative protocols as networks expanded.
- The data link layer, layer 2 in the protocol stack, plays a crucial role in managing links between computers and facilitating data transmission.
- Data delineation is essential for marking the start and end of packets, as well as distinguishing between fields within a frame.
- Media access control determines who can access and transmit data on the physical medium, resolving contention among multiple devices.
- Error control on the data link layer ensures data integrity during transmission, with techniques like parity, cyclic redundancy codes, and Hamming codes providing error detection and correction capabilities.