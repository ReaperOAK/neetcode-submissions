class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cm={i : [] for i in range(numCourses)}
        for a,b in prerequisites:
            cm[a].append(b)
        
        v,c=set(),set()
        res=[]
        def dfs(crs):
            if crs in c: return False
            if crs in v: return True
            c.add(crs)
            for pre in cm[crs]:
                if not dfs(pre): return False
            c.remove(crs)
            v.add(crs)
            res.append(crs)
            
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
            
