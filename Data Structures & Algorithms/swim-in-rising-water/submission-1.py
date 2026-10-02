class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        minh=[[grid[0][0],0,0]]
        visit.add((0,0))
        while minh:
            t,r,c = heapq.heappop(minh)
            if r==n-1 and c==n-1: return t
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if min(nr,nc)<0 or nr==n or nc==n or (nr,nc) in visit: continue
                visit.add((nr,nc))
                heapq.heappush(minh,[max(t,grid[nr][nc]),nr,nc])