class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if (x-y)!=0:
                heapq.heappush(stones, (x-y))
        stones.append(0)
        return abs(stones[0])