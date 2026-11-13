class Solution:
    def countSubstrings(self, s: str) -> int:
        def check_pal(l,r):
            res = 0
            while l>=0 and r<len(s) and s[r]==s[l]:
                l-=1
                r+=1
                res+=1
            return res
        res = 0
        for i in range(0, len(s)):
            res+=check_pal(i, i)
            res+=check_pal(i, i+1)
        return res