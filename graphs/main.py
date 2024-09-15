import heapq
from collections import deque


def dfs(root, graph):
    stack = [root]
    visited = set()

    while stack:
        current = stack.pop()

        if current not in visited:
            print(current, end="")
            visited.add(current)

        neighbor = set(graph[current])
        stack.extend(neighbor - visited)


def bfs(root, graph):
    queue = deque([root])
    visited = set()

    while queue:
        current = queue.popleft()
        if current not in visited:
            print(current, end="")
            visited.add(current)

        neighbor = set(graph[current])
        queue.extend(neighbor - visited)


def dijkstra(root, graph):
    priority_queue = []
    distances = {node: float("inf") for node in graph}
    distances[root] = 0
    heapq.heappush(priority_queue, (0, root))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    print(distances)


if __name__ == "__main__":
    adj_list = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    weighted_adj_list = {
        "A": [("B", 2), "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    dfs("A", adj_list)
    print("\n")
    bfs("A", adj_list)

    dijkstra("A", adj_list)
