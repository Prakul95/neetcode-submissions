class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(index, temp):
            if index == len(nums):
                return 
            res.append(temp[:])
            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(i+1, temp[:])
                temp.pop()
            return 
        
        dfs(-1, [])
        return res
            
