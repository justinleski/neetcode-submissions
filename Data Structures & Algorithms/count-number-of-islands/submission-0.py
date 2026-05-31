class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # using hash set since we dont need to map anything
        count = 0

        for i, row in enumerate(grid):
            for j, col in enumerate(row):

                # print(str(i)+ " - " +str(j))
                #print(int(grid[i][j]) == 1)
                # needs to be cast as int


                if (int(grid[i][j]) == 1 and (int(i),int(j)) not in visited):
           
                    count += 1
                    self.recursiveDfs(i, j, visited, grid)
                
                # elif (int(grid[i][j]) == 0):
                #     self.recursiveDfs(i, j, visited, grid)

        return count

    def recursiveDfs(self, row, col, visited, grid):
        i = int(row)
        j = int(col)

        if (i,j) in visited:
            # skip
            return

        # otherwise we mark spot as visited (add to hash set)
        visited.add((i,j))


        # for each neighbour of the vertex, call recusrive dfs if matches (isl or water)
        if (i+1) < len(grid) and int(grid[i][j]) == int(grid[i+1][j]): # m, width
            self.recursiveDfs(i+1, j, visited, grid)

        if (j+1) < len(grid[0]) and int(grid[i][j]) == int(grid[i][j+1]): # n, length
            self.recursiveDfs(i, j+1, visited, grid)

        if (j-1) >= 0 and int(grid[i][j]) == int(grid[i][j-1]):
            self.recursiveDfs(i, j-1, visited, grid)

        if (i-1) >= 0 and int(grid[i][j]) == int(grid[i-1][j]):
            self.recursiveDfs(i-1, j, visited, grid)

# class Solution:
#     def dfs():


#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         # we need hash set to prevent cycles / track visited
#         visited = {} # store as (i,j)
#         islandCount = 0

#         for i, row in enumerate(grid):

#             for j, col in enumerate(row):

#                 if (i,j) in visited:
#                     continue

#                 elif col == 1:
#                     # we find one island, then ensure all other adjacent 1s marked as visited
#                     islandCount += 1

#                     # here is where DFS is performed
#                     dfs(i,j) # TODO: actually implement lol

                