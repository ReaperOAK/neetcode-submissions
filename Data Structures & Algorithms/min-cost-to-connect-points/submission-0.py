class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node= len(points), 0
        dist=[10000000]*n
        visit=[False]*n
        edge,res=0,0

        while edge<n-1:
            visit[node]=True
            nn=-1
            for i in range(n):
                if visit[i]: continue
                cd=(abs(points[i][0]-points[node][0]) + abs(points[i][1]-points[node][1]))
                dist[i]=min(dist[i],cd)
                if nn==-1 or dist[i]<dist[nn]:
                    nn=i
            
            res+= dist[nn]
            node=nn
            edge+=1

        return res