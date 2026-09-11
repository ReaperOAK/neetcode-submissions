class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distNidx=[]
        for x,y in points:
            dist=(x**2)+(y**2)
            distNidx.append([dist,x,y])

        heapq.heapify(distNidx)
        res=[]
        while k>0:
            dist,x,y=heapq.heappop(distNidx)
            res.append([x,y])
            k-=1
        return res