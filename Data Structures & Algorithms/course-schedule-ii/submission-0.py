class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        schedule = []
        adj = defaultdict(list)

        # if no prereqs, we can take any courses in any order for num of courses
        if not prerequisites:
            for i in range(numCourses):
                schedule.append(i)
            return schedule

        for i in range(numCourses):
            adj[i] = []

        for u,v in prerequisites:
            adj[v].append(u)

        visited = {} # True currently visiting, False visited
      

        def dfs(node):

            if node in visited:
                return visited[node]

            visited[node] = True

            for nei in adj[node]:
                if dfs(nei) == True: # i.e. if actively visiting
                    return True
                
            visited[node] = False
            schedule.append(node)

        for node in list(adj):
            if dfs(node) == True:
                return []

        # ensure all dependent classes are reversed
        schedule.reverse()
 
        return schedule