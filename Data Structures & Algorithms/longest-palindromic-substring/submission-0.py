class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # we start from the center and compare the chars on left and right and keep computing the result for max
        # for odd cases we could start from i and i+1 

        def check_pal(l,r):
            while l>=0 and r<len(s) and s[r]==s[l]:
                l-=1
                r+=1
            return s[l+1:r]
        res = ""
        for i in range(0, len(s)):
            res = max(check_pal(i,i), check_pal(i, i+1), res, key = len)
        return res
        

