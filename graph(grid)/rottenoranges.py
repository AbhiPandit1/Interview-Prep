# ye question easy to understand he to smjhaaonga ni step likhoonga
# phle jo jo value 2 ki he use apne queue me daal do
# phr bfs chlao normally with time ke saath bas time bb update krna hoga 
# and then normal bfs chalana he and uske baad check krna ki do we still have any  in our grid if yes then return -1
# else return timeclass 
# hum max_time ko outside the loop lete he kuki agr wo har baar run hoge queue me to max_time se compare krenge

# Solution:
   
   
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        def bfs():
            queue=[]

            for i in range(m):
                for j in range(n):
                    if grid[i][j]==2:
                        queue.append((i,j,0))
            max_time=0
            while queue:
                row,col,time=queue.pop(0)

                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                

                for dr,dc in directions:
                    newDr=dr+row
                    newDc=dc+col

                    if newDr >= 0 and newDr < m and newDc >= 0 and newDc < n and grid[newDr][newDc] == 1:
                        grid[newDr][newDc]=2
                        queue.append((newDr,newDc,time+1))
                        max_time=max(max_time,time+1)
            return max_time
        

        res=bfs()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return res
