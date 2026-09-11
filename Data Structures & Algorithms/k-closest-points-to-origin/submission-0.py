class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distNidx=[]
        res=[]
        for idx in range(len(points)):
            dist=math.sqrt((points[idx][0]**2) + (points[idx][1]**2))
            distNidx.append((dist,idx))

        heapq.heapify(distNidx)
        while k>0:
            point=heapq.heappop(distNidx)
            point=point[1]
            res.append((points[point]))
            k-=1
        return res