class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_count = 1
        for ele in nums:
            if ele-1 in nums:
                continue
            streak = ele
            count=0
            while streak in nums:
                count+=1
                streak+=1
            max_count = max(max_count, count)
        return max_count