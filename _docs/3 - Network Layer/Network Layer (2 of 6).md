# IPv4 Addressing (Network Layer)

## Definition
IPv4 (Internet Protocol version 4) addressing is a method of identifying devices on a network using an IPv4 address. 

## Structure of IPv4 Address
An IPv4 address is a 32-bit number that uniquely identifies a device on the network. It is typically written as four decimal numbers separated by periods, each representing eight bits of the address. For example, 192.168.1.1.

## Components of IPv4 Address
1. **Network ID:** The part of the IP address that identifies the specific network on which the device is located.
2. **Host ID:** The part of the IP address that identifies the specific device on the network.

## Subnetting
Subnetting is a method of dividing a network into two or more smaller networks. It involves taking bits from the host portion of the IP address to use for identifying the subnet.

## Classes of IPv4 Addresses
IPv4 addresses are divided into five classes (A, B, C, D, and E) based on the first four bits of the address. Classes A, B, and C are used for unicast addresses, Class D is used for multicast addresses, and Class E is reserved for future use.

## Role of IPv4 Addressing in the Network Layer
The Network Layer uses IPv4 addresses to identify the source and destination of each packet of data. It uses the network ID to route the packet to the correct network and the host ID to deliver the packet to the correct device.

#### Key Insights

- The class-based addressing scheme was used to allocate network and host portions of an address, but it has been replaced with a more flexible approach.
- Net masks indicate the network and host portions of an address, allowing for more efficient routing.
- Default gateways are used when there is no specific route for a packet, providing a way to send packets to other networks.
- Routing tables are used to determine the next hop for a packet based on its destination address, allowing for efficient packet forwarding.
- Private addresses are reserved for local use and are not routed across the internet, providing a way to create isolated networks.
- The 0.0.0.0 address is used as a placeholder for devices that do not have an assigned address yet.
- The 127.0.0.1 address, also known as localhost, is used for communication between programs on the same computer.