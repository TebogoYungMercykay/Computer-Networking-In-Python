# Routing and Addressing (Network Layer)

## Definition
Routing and addressing are key functions of the Network Layer in the OSI model. 

## Addressing
Addressing refers to the way that packets of data are labeled to indicate their source and destination. In an IP network, this involves the use of IP addresses, which uniquely identify each device on the network.

1. **IPv4:** The most widely used version of IP, uses 32-bit addresses.
2. **IPv6:** The next generation of IP, uses 128-bit addresses for increased address space.

## Routing
Routing is the process of selecting a path over which to send packets. Routers analyze the destination IP address of a packet and make decisions about where to send it next to get it closer to its destination.

1. **Static Routing:** Routes are manually set up by the network administrator. These routes do not change unless the network administrator changes them.
2. **Dynamic Routing:** Routes are determined by routing protocols. These routes can change as the network conditions change.

## Role of the Network Layer
The Network Layer is responsible for the delivery of individual packets from the source host to the destination host. This involves using IP addresses to label packets and routing algorithms to send them on the best path. The Network Layer is also responsible for handling packet fragmentation and error detection.

#### Key Insights

- Routing determines the path of data, while addressing identifies the destination. It is crucial for efficient data transmission.
- RIP and OSPF are popular routing protocols used in the TCP/IP context. They help determine the best routes for data transmission.
- IP, specifically IPv4, has been the primary protocol at layer 3 for many years. However, IPv6 is now being deployed as a replacement due to the limitations of IPv4.
- IPv4 has faced criticism and is considered broken by some. IPv6 is gradually taking over, although it will still take time for it to fully replace IPv4.
- Source routing, like bang addressing, was used in the early days of networking but is no longer in common use. It involved specifying the route for data transmission.
- Asynchronous Transfer Mode (ATM) is a protocol that establishes paths between nodes for constant throughput. It is used in multimedia contexts and by telephone companies.
- IPv5 was an experimental protocol that was never widely used, leading to the jump from IPv4 to IPv6. IPv6 is actively being deployed and will eventually replace IPv4.