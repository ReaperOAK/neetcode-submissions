class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p={i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            p[crs].append(pre)
        
        v=set()
        
        def dfs(crs):
            if crs in v:
                return False
            if p[crs]==[]:
                return True
            v.add(crs)
            for pre in p[crs]:
                if not dfs(pre):
                    return False
            v.remove(crs)
            p[crs]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True