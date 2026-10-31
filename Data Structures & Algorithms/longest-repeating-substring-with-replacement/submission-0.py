class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        max_count = 0
        count_dict = {}
        max_f = 0
        res = 0
        while r<len(s):
            if s[r] not in count_dict:
                count_dict[s[r]] = 1
            else:
                count_dict[s[r]]+=1
            max_f = max(max_f, count_dict[s[r]])
            while l<=r and r-l+1-max_f>k:
                count_dict[s[l]]-=1
                if count_dict[s[l]]==0:
                    del count_dict[s[l]]
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res
                
