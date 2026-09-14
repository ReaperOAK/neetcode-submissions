class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                temp=subset.copy()
                if temp in res:
                    return
                else:
                    res.append(temp)
                    return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res