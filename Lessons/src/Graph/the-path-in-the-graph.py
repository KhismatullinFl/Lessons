import sys
import collections

def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    start_node_based, end_node_based = map(int, input().split())
    start_node = start_node_based - 1
    end_node = end_node_based - 1
    
    if start_node == end_node:
        print(0)
        return
    
    distance = [-1] * n
    parent = [-1] * n
    distance[start_node] = 0
    queue = collections.deque([start_node])
    
    while queue:
        u = queue.popleft()
        for v in range(n):
            if matrix[u][v] == 1:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                    
    if distance[end_node] == -1:
        print("-1")
    else:
        print(distance[end_node])
        path = []
        current_node = end_node
        while current_node != -1:
            path.append(current_node)
            current_node = parent[current_node]
        path.reverse()
        path_based = [node + 1 for node in path]
        print(*(path_based))



if __name__ == '__main__':
    main()