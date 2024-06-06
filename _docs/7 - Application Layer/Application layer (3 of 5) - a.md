# Dijkstra's Algorithm (Application Layer)

## Definition
Dijkstra's Algorithm is a graph search algorithm that solves the shortest-path problem for a graph with non-negative edge path costs, producing a shortest path tree. This algorithm is often used in routing and as a subroutine in other graph algorithms.

## How Dijkstra's Algorithm Works
1. **Initialization:** Start at the source vertex, s. Mark the distance to it from itself as 0. For all other vertices, mark the distance from the source as infinity.
2. **Visit Vertex:** Visit the unvisited vertex with the smallest known distance from the source vertex.
3. **Update Distances:** For the current vertex, consider all of its unvisited neighbors. Calculate their tentative distances from the source. If the calculated distance of a vertex is less than the known distance, update the shortest distance.
4. **Mark as Visited:** Once we have visited all the unvisited neighbors of the current vertex, mark the current vertex as visited. A visited vertex will not be checked again.
5. **Repeat:** Continue this process until all the vertices in the graph have been visited.

## Dijkstra's Algorithm and the Application Layer
While Dijkstra's Algorithm is not an application layer protocol, it is used in the underlying network layers to provide services that the application layer uses. For example, OSPF (Open Shortest Path First), a common routing protocol that operates at the network layer, uses Dijkstra's Algorithm to calculate the shortest path for routing network packets. This directly impacts how data is transmitted and received in the application layer.

#### Key Insights

- Dijkstra's algorithm is used to find the shortest or cheapest path in a graph, considering the costs associated with the edges or links.
- The algorithm starts with a known node and gradually expands to include other nodes, selecting the cheapest options to reach them.
- The algorithm is greedy, always choosing the cheapest candidate at each step to ensure the best global solution.
- The tabular approach provides a practical implementation of the algorithm, allowing for easy manipulation of values and tracking of progress.
- The algorithm determines the optimal routes in a network, which can be used for packet routing and forwarding in computer networks.
- The video highlights the importance of considering only new candidates and discarding useless information to optimize the algorithm's efficiency.
- Reading the original paper on Dijkstra's algorithm can provide a more formal and comprehensive understanding of the topic.
