
# Compare BFS and DFS Performance

from collections import deque
import time

# Create a graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Breadth-First Search
def bfs(graph, start, goal):
    queue = deque([start])
    visited = []
    
    start_time = time.perf_counter()

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            if node == goal:
                break

            queue.extend(
                neighbor for neighbor in graph[node]
                if neighbor not in visited
            )

    elapsed = time.perf_counter() - start_time
    return visited, elapsed

# Depth-First Search
def dfs(graph, start, goal):
    stack = [start]
    visited = []

    start_time = time.perf_counter()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            if node == goal:
                break

            stack.extend(reversed(graph[node]))

    elapsed = time.perf_counter() - start_time
    return visited, elapsed

# Search for the goal node
start_node = 'A'
goal_node = 'H'

bfs_visited, bfs_time = bfs(graph, start_node, goal_node)
dfs_visited, dfs_time = dfs(graph, start_node, goal_node)

# Display results
print("BFS Results")
print("Visited Nodes:", bfs_visited)
print("Nodes Visited:", len(bfs_visited))
print("Execution Time:", round(bfs_time, 8), "seconds")

print("\nDFS Results")
print("Visited Nodes:", dfs_visited)
print("Nodes Visited:", len(dfs_visited))
print("Execution Time:", round(dfs_time, 8), "seconds")

print("\nPerformance Comparison")
if bfs_time < dfs_time:
    print("BFS was faster in this run.")
elif dfs_time < bfs_time:
    print("DFS was faster in this run.")
else:
    print("Both took approximately the same time.")
