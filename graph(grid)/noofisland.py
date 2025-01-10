# is question me grid me 1 dhoonhd he jo ki aapas me milsake means type of dfs krna he har trf se
# so isme hum visit ka bb use krskte he ya grid ko jo visit krlia 0 me convert krdenge
# isme return kch ni krna bas just dekhna he khaa tak move krskta he har ke lie
# if wo grid ek bbarr bb move krta he to use result me add krdenge

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m=len(grid)
        n=len(grid[0])

        def helper(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=="0" or (i,j) in visit:
                return 
            
            visit.add((i,j))
            directions=[[0,1],[0,-1],[1,0],[-1,0]]

            for dr,dc in directions:
                helper(i+dr,j+dc)
        

        result=0
        visit=set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visit:
                    helper(i,j)
                    result+=1
        return result

