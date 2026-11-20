class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def get_time(k):
            time = 0
            curr = 0
            for i in range(0,len(piles)):

                time += math.ceil(piles[i] / k)
            return time>h
        

        l = 1
        r = sum(piles)

        while l<r:

            mid = l + (r-l)//2
            if get_time(mid):
                l = mid + 1
            else:
                r = mid
        
        return l
            
        

