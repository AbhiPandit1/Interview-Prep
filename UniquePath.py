# is question me kuch ni krna normal template use krna he grid ka bas dhyaan rkhna he upr right jaa skte he
# simple template and them memoize it we want all the path so we will add the soln

#Time complexity:O(m*n) as we are visiting each cell once
#Space complexity:O(m*n) as we are using dp array

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helper(i,j):

            if i==m-1 and j==n-1:
                return 1
            
            if i>=m or j>=n or i<0 or j<0 or (i,j) in visit:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res=0
            visit.add((i,j))
            res+=helper(i+1,j)+helper(i,j+1)

            visit.remove((i,j))

            dp[(i,j)]= res
            return dp[(i,j)]
        visit=set()
        dp={}
        return helper(0,0)