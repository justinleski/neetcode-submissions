class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # find rotten fruit O(m*n) time
        rotten = []
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    freshCount += 1

        # since we cannot rot when rotten doesnt exist
        if freshCount > 0 and not rotten:
            return -1
        elif not rotten:
            return 0


        # immediate bfs
        queue = deque()
        for rot in rotten:
            queue.append(rot)


        minutes = -1 # because the first "minute" is initial rotten fruit

        while queue:
            minutes += 1
            queueLen = len(queue)
  
            for _ in range(queueLen):
                i, j = queue.popleft()

                if i + 1 < len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i+1, j))
                    freshCount -= 1

                if i - 1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append((i-1, j))
                    freshCount -= 1

                if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append((i, j+1))
                    freshCount -= 1

                if j - 1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append((i, j-1))
                    freshCount -= 1

        if freshCount > 0:
            return -1

        return minutes



