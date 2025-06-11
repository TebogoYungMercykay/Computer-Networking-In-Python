# Token Passing (Data Link Layer)

## Definition
Token passing is a network access method used in some types of networks to control access to a shared communication medium. It involves circulating a special data packet called a token among network nodes to manage which device can transmit data at any given time. This method helps prevent data collisions and ensures fair access for all devices on the network.

## How it Works
1. **Token:** The token is a small data packet that travels around the network. It acts as a permission slip that grants a node the right to transmit data.
2. **Transmission:** When a node receives the token, it checks if it has data to send. If it does, it captures the token, attaches its data to the token, and then sends the combined data-token to the next node in the network.
3. **Reception:** The data-token travels through the network until it reaches the destination node. The destination node extracts the data from the token and releases the token back into the network for other nodes to use.

## Types of Token Passing
### Token Ring
- **Topology:** Nodes are connected in a circular (ring) configuration. Each node is connected to two other nodes, forming a closed loop.
- **Operation:** The token circulates around the ring in one direction. When a node has data to send, it waits for the token, attaches its data to the token, and then sends it around the ring to the intended recipient. After the data is received, the token continues to circulate.

### Token Bus
- **Topology:** Nodes are connected in a linear or bus configuration, where all nodes share a common communication line.
- **Operation:** The token is passed along the bus. When a node receives the token and has data to send, it captures the token, attaches its data, and sends the data-token to the next node in line. The token circulates from one end of the bus to the other.

## Role of Token Passing in the Data Link Layer
The Data Link Layer is responsible for controlling access to the shared communication medium in a network. Token passing is one of the methods used to manage this access. It ensures that all devices have a fair opportunity to transmit data and helps to prevent collisions.

### Key Insights

- **Orderly Communication:** Token ring networks ensure that only one node can transmit data at a time, providing orderly communication and avoiding collisions.
  
  *Example:* Imagine a roundtable discussion where only the person holding a talking stick can speak. This ensures no one talks over anyone else, similar to how token passing ensures orderly data transmission.

- **Cost and Competition:** Token ring networks were more expensive compared to Ethernet networks. As Ethernet technology advanced, it became faster and cheaper, leading to wider adoption.

  *Example:* Token ring networks were like high-end exclusive clubs—prestigious but costly. Ethernet networks were like popular community centers—affordable and widely accessible.

- **Resilient Connections:** In token ring networks, a wiring hub called a Multi-station Access Unit (MAU) maintains the integrity of the ring. If a computer is turned off, the MAU bridges the gap, ensuring the network continues to function without interruption.

  *Example:* Think of the MAU as a relay runner in a race. If one runner stops, the baton (data) is passed smoothly to the next runner, keeping the race going without a hitch.

- **Active Monitor:** An active monitor in a token ring network ensures the token is not lost. If the token is lost, the active monitor regenerates it. If the active monitor goes offline, an election process is initiated to select a new monitor.

  *Example:* In a well-organized office, if the supervisor (active monitor) leaves, the team elects a new supervisor to ensure work continues smoothly.

- **Priority and Fairness:** Token ring networks can assign priorities to certain stations, allowing them to reserve the token for transmission. This prioritization can sometimes lead to lower priority stations waiting longer to send data, affecting fairness.

  *Example:* In a meeting, if certain members have more speaking privileges, others might have to wait longer to share their ideas, which can be seen as unfair.

- **Scalability Issues:** Token ring networks face challenges in large-scale networks due to the inefficiency of passing a single token around a long ring. For larger networks, protocols like Fiber Distributed Data Interface (FDDI) were developed to address these limitations.

  *Example:* Passing a note around a small group is quick and easy, but in a large auditorium, it becomes inefficient. Similarly, token ring is efficient for small to medium networks but not for large ones.

- **Media Access Control:** Effective media access control is crucial for preventing collisions and ensuring smooth data transmission. Token passing is one of several methods (alongside CSMA/CD used in Ethernet) to manage this.

  *Example:* In a busy kitchen, chefs take turns using shared appliances to avoid clashes. Token passing acts like a kitchen schedule, ensuring each chef gets their turn without chaos.
  