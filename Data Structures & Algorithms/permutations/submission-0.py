class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(index, temp):

            if index==len(nums):
                res.append(temp[:])
                return 
            for i in range(index, len(nums)):
                temp[i], temp[index]=temp[index], temp[i]
                dfs(index+1, temp[:])
                temp[index], temp[i]=temp[i], temp[index]
        dfs(0, nums)
        return res