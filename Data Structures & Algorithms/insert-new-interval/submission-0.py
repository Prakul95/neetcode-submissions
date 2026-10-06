class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        
        res = []
        intervals.append(newInterval)
        for i in range(0, len(intervals)):
            if intervals[i][0]>=intervals[-1][0]:
                intervals[i], intervals[-1]=intervals[-1], intervals[i]

        for i in range(0, len(intervals)):
            if res and res[-1][1]>=intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res