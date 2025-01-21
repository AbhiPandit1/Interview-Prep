# bfs ka achha question he ek grid he jisme 1 he to water cell he and 0 he to land 
# and hame usme se highest peak nikalna he jisme absolute diff aapase not more than one ho neighbour cell me
# kuch ni krna bfs run krna he jo jo 1 he usse queue me append kro aur height[i][j] = 0 krdo
# and then mile to usse queue me append kro and height[i][j] = height[x][y] + 1 krdo

from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        # Initialize the result matrix with -1 for unvisited cells
        heights = [[-1 for _ in range(n)] for _ in range(m)]
        
        def bfs():
            queue = []
            
            # Initialize the queue with all water cells
            for i in range(m):
                for j in range(n):
                    if isWater[i][j] == 1:
                        queue.append((i, j))
                        heights[i][j] = 0  # Water cells have height 0
            
            # BFS to propagate the heights
            while queue:
                i_, j_ = queue.pop(0)
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]  # Adjacent cells
                
                for dx, dy in directions:
                    i__ = i_ + dx
                    j__ = j_ + dy
                    
                    # Check if the cell is within bounds and unvisited
                    if 0 <= i__ < m and 0 <= j__ < n and heights[i__][j__] == -1:
                        heights[i__][j__] = heights[i_][j_] + 1
                        queue.append((i__, j__))
        
        bfs()
        return heights
