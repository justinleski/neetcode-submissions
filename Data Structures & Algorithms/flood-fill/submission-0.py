class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        # edge case - will exceed memory as we'll infinitely loop; no need to attempt to fill with colour itself
        if color == image[sr][sc]:
            return image

        # how do we find the neighbours of sr,sc. what data structure to compose
        fillVal = image[sr][sc]
        queue = deque() # bfs

        queue.append((sr,sc))

        while queue:

            currSr, currSc = queue.popleft()
            
            if image[currSr][currSc] == fillVal:
                image[currSr][currSc] = color
            else:
                continue

            # check all neighbours
            if currSr + 1 < len(image) and image[currSr + 1][currSc] == fillVal:
                queue.append((currSr + 1, currSc))
            
            if currSr - 1 >= 0 and image[currSr - 1][currSc] == fillVal:
                queue.append((currSr - 1, currSc))

            if currSc + 1 < len(image[0]) and image[currSr][currSc + 1] == fillVal:
                queue.append((currSr, currSc + 1))

            if currSc - 1 >= 0 and image[currSr][currSc - 1] == fillVal:
                queue.append((currSr, currSc - 1))

        return image