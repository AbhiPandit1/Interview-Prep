# isme bb reverse thinking krni he
# start krna he phle dono row ke boundaries as they will reach atleast one side and jab jab usse chota mile flow krte 
# jana hai for row we will go to 0-->r and for down one we will go heightof col-1-->r and this will also be our prev
# bas check krlenea he ki dono set me konsi value present hai jo hogi returne krdena he


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m=len(heights)
        n=len(heights[0])


        def helper(i,j,visit,prev):
            if i>=m or j>=n or i<0 or j<0 or (i,j) in visit or heights[i][j]<prev:
                return 
            visit.add((i,j))

            directions=[[0,1],[0,-1],[1,0],[-1,0]]

            for dr,dc in directions:
                helper(i+dr,j+dc,visit,heights[i][j])
            

        atl=set()
        pac=set()
        for r in range(n):
            helper(0, r, pac, heights[0][r])  # First row
            helper(m - 1, r, atl, heights[m - 1][r])  # Last row
        for c in range(m):
            helper(c, 0, pac, heights[c][0])  # First column
            helper(c, n - 1, atl, heights[c][n - 1])  # Last column

        
        res=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in atl and (i,j) in pac:
                    res.append((i,j))
        return res
        
        