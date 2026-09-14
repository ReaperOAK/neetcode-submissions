class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        subset=[]
        def dfs(o,c):
            if o==c==n:
                res.append(''.join(subset))
                return
            if o<n:
                subset.append("(")
                dfs(o+1,c)
                subset.pop()
            if c<o:
                subset.append(")")
                dfs(o,c+1)
                subset.pop()
        dfs(0,0)
        return res

