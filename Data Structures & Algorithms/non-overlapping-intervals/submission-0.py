class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort()
        res = 0
        prev = None
        for i in range(0, len(intervals)):

            if prev and prev>intervals[i][0]:
                res+=1
                prev = min(prev, intervals[i][1])
            else:
                prev = intervals[i][1]
        return res