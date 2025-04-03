import sys

def main():
    n = int(sys.stdin.readline())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    li = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                li[i].append(j)

    visited = [False] * n
    parent = [-1] * n
    cycle_path = []

    def find_cycle(u, p):
        visited[u] = True
        for v in li[u]:
            if v == p:
                continue
            if visited[v]:
                cycle_path.append(v)
                cycle_path.append(u)
                curr = u
                while parent[curr] != -1 and parent[curr] != v:
                    cycle_path.append(parent[curr])
                    curr = parent[curr]
                return True
            else:
                parent[v] = u
                if find_cycle(v, u):
                    return True
        return False

    has_cycle = False
    for i in range(n):
        if not visited[i]:
            if find_cycle(i, -1):
                has_cycle = True
                break

    if has_cycle:
        print("YES")
        cycle_path = cycle_path[::-1]
        first_node = cycle_path[0]
        cycle = []
        start_index = -1
        for i in range(len(cycle_path)):
            if cycle_path[i] == first_node:
                start_index = i
                break
        for i in range(start_index, len(cycle_path)):
            if cycle_path[i] not in cycle:
                cycle.append(cycle_path[i])
            if cycle_path[i] == cycle_path[-1] and i != len(cycle_path) -1 and cycle_path[i+1] == first_node:
                break
        print(len(cycle))
        print(*(x + 1 for x in cycle))
    else:
        print("NO")

if __name__ == '__main__':
    main()
