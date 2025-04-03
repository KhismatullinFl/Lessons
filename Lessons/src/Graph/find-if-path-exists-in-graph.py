class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]
    
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        if source == destination:
            return True
        
        queue = [source]
        visited = [False] * n
        visited[source] = True
        
        while queue:
            current = queue.pop(0)
            for i in graph[current]:
                if i == destination:
                    return True
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
        
        return False