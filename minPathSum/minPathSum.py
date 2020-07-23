class Solution:
    def minPathSum(self, grid:list) -> int:
        ncol = len(grid)  # 获取矩阵列数
        nrow = len(grid[0])  # 获取矩阵行数
        dp = [[0] * nrow for i in range(ncol)]  # 生成和原矩阵同阶的临时矩阵dp
        dp[0][0] = grid[0][0]
        for i in range(1,nrow):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,ncol):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, nrow):
            for j in range(1, ncol):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[nrow-1][ncol-1]




if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution()
    print(s.minPathSum(grid))