class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1

        while l<r:
            sum_total = numbers[l]+numbers[r]
            if sum_total<target:
                l +=1
                continue
            elif sum_total>target:
                r -=1 
                continue
            else:
                return [l+1,r+1]
        return [-1,-1]