# same as no if island bas isme hume res=1 leke use helper(function me add krwana he everytime recursion is called)
# and then max_area to aata hihoga

def maxAreaOfIsland(grid):
    m, n = len(grid), len(grid[0])

    def helper(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0  # Mark cell as visited
        res = 1  # Current cell
        
        # Accumulate areas of neighbors
        for dr, dc in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            res += helper(i + dr, j + dc)
        
        return res

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, helper(i, j))
    
    return max_area
