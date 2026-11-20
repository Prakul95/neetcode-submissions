class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def bin_search(l,r):

            while l<=r:
                mid = l + (r-l)//2
                if nums[mid]<target:
                    l = mid + 1
                elif nums[mid]>target:
                    r = mid -1
                else:
                    return mid
            return -1
        

        l = 0 
        r = len(nums)-1

        while l<r:
            mid = l + (r-l)//2
            if nums[mid]>nums[-1]:
                l = mid + 1
            else:
                r = mid
        # print(l)
        ans = bin_search(0, l)
        if ans !=-1:
            return ans
            # return True
        return bin_search(l,len(nums)-1)

            