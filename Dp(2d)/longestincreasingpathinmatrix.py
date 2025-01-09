# iss question me hume longest increasing path khojna he matrix me
# so normal grid base case as we are going through every point in loop and then updating it then no need for visit
# 1+max(up,down,left,right) and then memoize it
# aur loop me max nikalo


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m=len(matrix)
        n=len(matrix[0])

        if not matrix:
            return 0
        
        def helper(i,j,prev):

            if i>=m or j>=n or i<0 or j<0 or matrix[i][j]<=prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)]= 1 + max(
                helper(i + 1, j, matrix[i][j]),  # Down
                helper(i - 1, j, matrix[i][j]),  # Up
                helper(i, j + 1, matrix[i][j]),  # Right
                helper(i, j - 1, matrix[i][j])   # Left
            )
            return dp[(i,j)]

         
        count=0
        dp={}

        for i in range(m):
            for j in range(n):
                count=max(count,helper(i,j,-1))
        
        return count