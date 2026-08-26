class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()

        l = 0
        r = 0
        max_val = 0
        while r<len(s):
            
            while s[r] in char_set and l<r:
                char_set.remove(s[l])
                l+=1
            
            char_set.add(s[r])

            max_val = max(max_val, r-l+1)
            r+=1
        return max_val
             
                    

                