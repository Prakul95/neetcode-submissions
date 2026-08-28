class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, curr, temp):

            if index == len(nums):
                return 
            if curr==target:
                res.append(temp[:])
                return 
            for i in range(index, len(nums)):
                if curr+nums[i]>target:
                    return
                temp.append(nums[i])
                dfs(i, curr+nums[i], temp[:])
                temp.pop()
            return 
        dfs(0,0,[])
        return res