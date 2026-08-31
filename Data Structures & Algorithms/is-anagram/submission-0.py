class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars={}
        for c in s:
            chars[c]=chars.get(c,0)+1
        chars2={}
        for c in t:
            chars2[c]=chars2.get(c,0)+1
        if chars==chars2:
            return True
        else:
            return False