class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [[None for _ in range(n)] for _ in range(m)]
        cache[-1][-1] = 1 # not necessary
   
        

        def memo(cache, r, c):

            # if we reach base case
            if r == m-1 or c == n-1:
                return 1 # i.e. 1

            elif cache[r][c] != None:
                return cache[r][c]

            elif cache[r][c] == None:
                cache[r][c] = (memo(cache, r+1, c) + memo(cache, r, c+1))
                return cache[r][c]

        # start at 0,0 in the grid
        return memo(cache, 0, 0)










        # for row in range(m):
        #     for col in range(n):

        #         cell = grid[row][col]

        #         # yo
        #         if cell != 0:
        #             #mark it visited
        #             grid[row][col] = 1