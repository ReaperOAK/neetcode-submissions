class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water=0
        l,r=0,len(heights)-1
        while l<r:
            width=r-l
            mh=min(heights[l],heights[r])
            curr=mh*width
            water=max(curr,water)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return water