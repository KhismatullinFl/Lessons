import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    M = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(input[ptr])
        v = int(input[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    visited = [False] * (N + 1)
    components = []

    for node in range(1, N + 1):
        if not visited[node]:
            queue = deque()
            queue.append(node)
            visited[node] = True
            component = []
            while queue:
                current = queue.popleft()
                component.append(current)
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            components.append(component)

    print(len(components))
    for component in components:
        print(len(component))
        print(' '.join(map(str, sorted(component))) + ' ')

if __name__ == "__main__":
    main()
