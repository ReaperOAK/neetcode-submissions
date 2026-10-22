class Solution:
    def climbStairs(self, n: int) -> int:
        f,s=1,1
        t=1
        while t<=n:
            f,s=s+f,f
            t+=1
        return s