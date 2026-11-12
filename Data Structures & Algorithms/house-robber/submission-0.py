class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # we are given houses in order and the amount of money is given in that order
        # we need to figure out how we can maximise the profit from the house robbery
        # we can either include the house in our max and we need to skip if we have two consecutive houses.
        # temp = max_amount
        # max_amount = max(last+cur, max_amount)
        # last = max(temp, last)


        last = 0
        max_amount = 0

        for curr in nums:
            temp = max_amount
            max_amount = max(last+curr, max_amount)
            last = max(temp, last)
        
        return max_amount