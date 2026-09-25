class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        em=[[] for _ in range(n)]
        for a,b in edges:
            em[a].append(b)
            em[b].append(a)
        visited=[False]*n
        def dfs(node):
            for nei in em[node]:
                if not visited[nei]:
                    visited[nei]=True
                    dfs(nei)
        
        count=0

        for node in range(n):
            if not visited[node]:
                visited[node]=True
                dfs(node)
                count+=1
        
        return count