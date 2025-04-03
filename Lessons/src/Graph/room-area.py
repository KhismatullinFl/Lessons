import sys

def dfs(x, y, labyrinth, visited):
        if x < 0 or x >= len(labyrinth) or y < 0 or y >= len(labyrinth[0]) or labyrinth[x][y] == '*' or visited[x][y]:
            return 0
        visited[x][y] = True
        count = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            count += dfs(x + dx, y + dy, labyrinth, visited)
        return count

def main():
    N = int(input().strip())
    labyrinth = [input().strip() for _ in range(N)]
    start_row, start_col = map(int, input().strip().split())
    start_row -= 1 
    start_col -= 1  

    visited = [[False] * N for _ in range(N)]
    area = dfs(start_row, start_col, labyrinth, visited)
    print(area)



if __name__ == '__main__':
    main()