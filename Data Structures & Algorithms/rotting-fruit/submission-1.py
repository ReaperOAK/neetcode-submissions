class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        rotten=set()
        fresh=set()
        q=deque()
        def rot(r,c):
            if min(r,c)<0 or r>=R or c>=C or (r,c) in rotten or grid[r][c]==0: return
            rotten.add((r,c))
            grid[r][c]=2
            fresh.remove((r,c))
            q.append([r,c])
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    q.append([r,c])
                    rotten.add((r,c))
                if grid[r][c]==1:
                    fresh.add((r,c))

        time=0
        while q and fresh:
            for _ in range(len(q)):
                r,c=q.popleft()            
                for (i,j) in [(0,1),(0,-1),(1,0),(-1,0)]:
                    rot(r+i,c+j)
            time+=1
        return time if len(fresh)==0 else -1