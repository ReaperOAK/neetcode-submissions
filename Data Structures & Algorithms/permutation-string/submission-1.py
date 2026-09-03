class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        l=0
        s1=sorted(s1)
        for r in range(len(s1),len(s2)+1):
            cw=sorted(s2[l:r])
            if s1==cw:
                return True
            l+=1
        return False