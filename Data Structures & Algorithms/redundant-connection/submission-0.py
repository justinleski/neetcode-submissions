class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) # +1 on n since we label nodes 1-n
        parent = [i for i in range(n + 1)]
        rank = [1] * (n+1)

        # keep moving up until we reach the parent, parent points to itself
        def find(n1):
            result = n1

            while result != parent[result]:
                parent[result] = parent[parent[result]] # compression: optimizes UF by halving
                result = parent[result]
            return result

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1


        for u,v in edges:
            if not union(u,v):
                return[u,v]




        # # adjacency list
        # adj = defaultdict(list)
        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
