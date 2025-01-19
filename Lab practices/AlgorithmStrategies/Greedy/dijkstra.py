import heapq


def dijkstra(graph, start):
    # Initialize the distance to all nodes as infinity and distance to the start node as 0
    distances = {node: float('infinity') for node in graph}
    print(distances)
    distances[start] = 0

    # Priority queue to store the nodes to be processed
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the distance is greater than the currently known distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print(f"Shortest distances from {start_node}: {distances}")
