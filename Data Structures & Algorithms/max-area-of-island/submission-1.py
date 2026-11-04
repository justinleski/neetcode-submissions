class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j, totalVisits):
            
            if (i,j) in visited:
                return totalVisits

            visited.add((i,j))
            totalVisits += 1

            # right horiz
            if i+1 < len(grid) and 1 == grid[i+1][j]:
                totalVisits = dfs(i+1, j, totalVisits)
    
            # left horiz
            if i-1 >= 0 and 1 == grid[i-1][j]:
                totalVisits = dfs(i-1, j, totalVisits) 
     
            # down vert
            if j+1 < len(grid[0]) and 1 == grid[i][j+1]:
                totalVisits = dfs(i, j+1, totalVisits)
     
            # up vert
            if j-1 >= 0 and 1 == grid[i][j-1]:
                totalVisits = dfs(i, j-1, totalVisits)
            
            return totalVisits


        visited = set()
        islandAreas = []

        for i, row in enumerate(grid):

            for j, col in enumerate(row):

                # only dfs on islands
                if grid[i][j] == 1 and (i,j) not in visited:
                    totalVisits = dfs(i, j, 0)
                    islandAreas.append(totalVisits)

        if islandAreas:
            return max(islandAreas)
        else:
            return 0




        