class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for i in range(0, len(points)):

            distance = -(points[i][0]**2 + points[i][1]**2)
            if len(heap)>=k:
                heapq.heappushpop(heap, [distance, points[i]])
            else:
                heapq.heappush(heap, [distance, points[i]])
        
        return [points for _, points in heap]