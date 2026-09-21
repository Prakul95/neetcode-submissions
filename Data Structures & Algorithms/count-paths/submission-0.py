class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        # we can only move right or down, that mean to reach the right most corner, we just have 1 way = right>right>right
        # and same for first - down row, down down down
        # if we can create a dp[] array which will store these unique combinations, 
        # we can count how many ways are there to reach dp[i][j] = dp[i-1][j] + dp[i][j-1]

        dp = [[0 for _ in range(n) ] for _ in range(m)]

        for i in range(0, m):
            dp[i][0]=1
        for j in range(0,n):
            dp[0][j]=1
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j]= dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]