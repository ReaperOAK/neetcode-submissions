class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        
        def findParent(node):
            if parent[node]!=node:
                parent[node]=findParent(parent[node])
            return parent[node]

        def union(a,b):
            p1,p2=findParent(a),findParent(b)
            if p1==p2: return False
            else: 
                parent[p1]=p2
                return True
        
        for u,v in edges:
            if not union(u,v): return [u,v]
        return []