# Token Passing (Data Link Layer)

## Definition
Token passing is a method of managing access to a shared medium in a network. It is used in some types of networks to prevent collisions and to ensure all devices get fair access.

## How it Works
1. **Token:** A special type of frame, called a token, is continuously passed around the network from one node to the next.
2. **Transmission:** When a node receives the token and has data to send, it captures the token, attaches data to it, and then sends this data-token on to the next node in the network.
3. **Reception:** The data-token continues to be passed along the network until it reaches its destination, where the data is removed and the token is released back into the network.

## Types of Token Passing
1. **Token Ring:** In a token ring network, the nodes are arranged in a logical ring, and the token is passed from each node to the next in a circular manner.
2. **Token Bus:** In a token bus network, the nodes are arranged in a logical bus, and the token is passed along the bus.

## Role of Token Passing in the Data Link Layer
The Data Link Layer is responsible for controlling access to the shared medium in a network. Token passing is one method it can use to manage this access, ensuring that all devices get a turn to transmit and helping to prevent collisions.

#### Key Insights

- Token ring networks use a ring topology and token passing to ensure orderly communication. This provides a feeling of safety as only one node can speak at a time.
- Token ring networks did not survive due to the higher costs compared to Ethernet and the continuous development of faster multiple access networks.
- The wiring hub in a token ring network bridges the connection when a computer is switched off, preventing the ring from breaking. This ensures uninterrupted communication.
- An active monitor in a token ring network is responsible for regenerating the token if it is lost. It also initiates an election process to select a new monitor if the current monitor goes offline.
- Token ring networks allow stations to have priorities and reserve the token for transmission. However, this can lead to lower priority stations not getting a chance to speak, impacting fairness.
- Token ring networks are not suitable for large-scale networks due to the limitations of passing a single token around a long ring. Alternative protocols like FDDI have been developed for larger networks.
- Media access control or contention control is crucial for nodes sharing a medium to effectively coordinate their access and prevent collisions or chaos in transmission.