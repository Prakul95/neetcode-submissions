class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        directions = [[0,1],[0,-1], [-1,0], [1,0]]
        rowLen = len(grid)
        colLen = len(grid[0])
        seen_set = set()
        q = deque()
        for i in range(0, rowLen):
            for j in range(0, colLen):
                if grid[i][j]==0:
                    q.append([i,j])
        def bfs(q):
            distance = 1
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    r,c = q.popleft()
                    if (r,c) in seen_set:
                        continue
                    seen_set.add((r,c))
                    for dr, dc in directions:
                        row = r+dr
                        col = c+dc
                        if 0<=row<rowLen and 0<=col<colLen and grid[row][col]==2147483647 and (row, col) not in seen_set:
                            
                            grid[row][col]=distance
                            q.append([row,col])
                        
                            
                distance+=1
        bfs(q)
        return 
                




            