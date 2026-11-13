class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # you cannot rob two houses adjacent to each other and we cannot rob two houses at the last and front of the list
        # 

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        max_val = 0
        last = 0
        for curr in nums:

            temp = max_val
            max_val = max(curr+last, max_val)
            last = max(temp, last)
        return max_val
        