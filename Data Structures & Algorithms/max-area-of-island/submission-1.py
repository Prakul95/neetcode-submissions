class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0], [0,1],[-1,0],[0,-1]]
        rowLen = len(grid)
        colLen = len(grid[0])
        seen_set = set()
        def bfs(i,j):

            q = deque()
            q.append([i,j])
            number_of_islands = 0
            while q:
                n = len(q)
                for _ in range(n):
                    r,c = q.popleft()
                    if (r,c) in seen_set:
                        continue
                    seen_set.add((r,c))
                    number_of_islands+=1
                    for dr, dc in directions:
                        row = dr + r
                        col = dc + c
                        if 0<=row<rowLen and 0<=col<colLen and (row,col) not in seen_set and grid[row][col]==1:
                            q.append([row,col])
                            
            return number_of_islands
        
        number_of_islands = 0

        for i in range(0, rowLen):
            for j in range(0,colLen):
                if grid[i][j]==1 and (i,j) not in seen_set:
                    number_of_islands = max(number_of_islands, bfs(i,j))
        return number_of_islands