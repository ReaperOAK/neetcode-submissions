class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                if len(subset)==len(nums):
                    res.append(subset.copy())
                    return
                else: return
            for j in range(len(nums)):
                if nums[j] in subset:
                    continue
                subset.append(nums[j])
                dfs(i+1)
                subset.pop()
                dfs(i+1)
        dfs(0)
        return res