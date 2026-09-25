class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        em=[[] for _ in range(n)]
        for a,b in edges:
            em[a].append(b)
            em[b].append(a)
        visited=set()
        def dfs(node):
            for nei in em[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        count=0

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                count+=1
        
        return count