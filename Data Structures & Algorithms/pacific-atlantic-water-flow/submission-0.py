class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C=len(heights),len(heights[0])
        P,A=set(),set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c,visit,pH):
            if (r,c) in visit or r<0 or c<0 or r>=R or c>=C or heights[r][c]<pH: return
            visit.add((r,c))
            for i,j in directions:
                dfs(r+i,c+j,visit,heights[r][c])
        
        for c in range(C):
            dfs(0,c,P,heights[0][c])
            dfs(R-1,c,A,heights[R-1][c])
        for r in range(R):
            dfs(r,0,P,heights[r][0])
            dfs(r,C-1,A,heights[r][C-1])

        res=[]
        for c in range(C):
            for r in range(R):
                if (r,c) in P and (r,c) in A:
                    res.append([r,c]) 

        return res
        