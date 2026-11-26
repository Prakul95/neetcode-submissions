class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index = {}
        for i in range(0, len(s)):

            last_index[s[i]]=i



        res = []
        size = 0
        end = 0
        for i in range(0, len(s)):

            size+=1
            end = max(last_index[s[i]], end)

            if i==end:
                res.append(size)
                size = 0
        return res




