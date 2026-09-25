class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(len(edges)+1)]

        def dfs(node,par):
            if visit[node]: return True
            visit[node]=True
            for nei in graph[node]:
                if nei==par: continue
                if dfs(nei,node): return True
            return False

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            visit=[False]*(len(edges)+1)
            if dfs(a,-1): return [a,b]
        return []
        
