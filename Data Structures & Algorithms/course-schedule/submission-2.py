class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True


        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u) # class u depends on class v first

        visited = {} # True if active (cycle), False is visited inactive
        courseCount = numCourses

        def dfs(node):
            nonlocal courseCount
            if node in visited:
                return visited[node]

            # currently on path
            visited[node] = True

            for nei in adj[node]:
                if dfs(nei): # if True that being visited actively, return False as cycle
                    return True 

            visited[node] = False
            courseCount -= 1
            return False #

        
        # just cycle detection - dfs
        for node in list(adj):
            if dfs(node) == True: # if cyclic dependency
                return False # false we cannot take all classes

        # print(courseCount)
        # if courseCount == 0:
        #     return True
        # return False
        return True