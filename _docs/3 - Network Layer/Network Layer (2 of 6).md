# IPv4 Addressing (Network Layer)

## Definition
IPv4 (Internet Protocol version 4) addressing is a method of identifying devices on a network using an IPv4 address. Each device on a network is assigned a unique IPv4 address to facilitate communication.

## Structure of IPv4 Address
An IPv4 address is a 32-bit number that uniquely identifies a device on the network. It is typically written as four decimal numbers separated by periods, each representing eight bits (or one byte) of the address. 

### Example:
- **IPv4 Address**: `192.168.1.1`

## Components of IPv4 Address
1. **Network ID:** The part of the IP address that identifies the specific network on which the device is located.
2. **Host ID:** The part of the IP address that identifies the specific device on the network.

### Example:
- For the IP address `192.168.1.1` with a subnet mask of `255.255.255.0`:
  - **Network ID**: `192.168.1.0`
  - **Host ID**: `0.0.0.1`

## Subnetting
Subnetting is a method of dividing a network into two or more smaller networks. It involves taking bits from the host portion of the IP address to use for identifying the subnet.

### Example:
- **Subnet Mask**: `255.255.255.0` indicates that the first three bytes (`192.168.1`) are the Network ID and the last byte (`0-255`) is used for Host IDs.

## Classes of IPv4 Addresses
IPv4 addresses are divided into five classes (A, B, C, D, and E) based on the first four bits of the address. Classes A, B, and C are used for unicast addresses, Class D is used for multicast addresses, and Class E is reserved for future use.

### Example:
- **Class A**: `1.0.0.0` to `126.0.0.0`
- **Class B**: `128.0.0.0` to `191.255.0.0`
- **Class C**: `192.0.0.0` to `223.255.255.0`
- **Class D**: `224.0.0.0` to `239.255.255.255` (multicast)
- **Class E**: `240.0.0.0` to `255.255.255.255` (reserved)

## Role of IPv4 Addressing in the Network Layer
The Network Layer uses IPv4 addresses to identify the source and destination of each packet of data. It uses the network ID to route the packet to the correct network and the host ID to deliver the packet to the correct device.

### Example:
- **Routing**: When a packet is sent from `192.168.1.2` to `10.0.0.5`, the Network Layer ensures the packet is routed from the `192.168.1.0` network to the `10.0.0.0` network, and then to the specific device with the host ID `5`.

## Key Insights

1. **Class-Based Addressing**: Initially, IPv4 used a class-based addressing scheme to allocate network and host portions of an address. However, this has been replaced with Classless Inter-Domain Routing (CIDR) for more flexible and efficient use of the address space.

    ### Example:
    - **CIDR Notation**: `192.168.1.0/24` indicates a subnet mask of `255.255.255.0`.

2. **Net Masks**: Net masks are used to indicate the network and host portions of an address, allowing for efficient routing.

    ### Example:
    - **Net Mask**: `255.255.255.0` for a `192.168.1.0` network.

3. **Default Gateways**: Default gateways are used when there is no specific route for a packet, providing a way to send packets to other networks.

    ### Example:
    - **Default Gateway**: `192.168.1.1` can be the gateway for the `192.168.1.0` network to access external networks.

4. **Routing Tables**: Routers use routing tables to determine the next hop for a packet based on its destination address, allowing for efficient packet forwarding.

    ### Example:
    - **Routing Table Entry**: A router might have an entry for `10.0.0.0/8` that specifies a next hop IP address for reaching any device on the `10.0.0.0` network.

5. **Private Addresses**: Certain IPv4 addresses are reserved for private use and are not routable on the public internet. These addresses are used within private networks.

    ### Example:
    - **Private Address Ranges**: `192.168.0.0 - 192.168.255.255`, `172.16.0.0 - 172.31.255.255`, `10.0.0.0 - 10.255.255.255`.

6. **0.0.0.0 Address**: This address is used as a placeholder for devices that do not have an assigned address yet.

    ### Example:
    - **Device Initialization**: A device might use `0.0.0.0` to indicate it has not yet been assigned an IP address.

7. **127.0.0.1 Address (Localhost)**: This address is used for communication between programs on the same computer.

    ### Example:
    - **Local Testing**: Developers use `127.0.0.1` to test web applications locally without involving external network traffic.

Understanding IPv4 addressing is crucial for configuring and managing network devices, ensuring efficient and accurate delivery of data across networks.