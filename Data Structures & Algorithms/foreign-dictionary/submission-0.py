class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {}

        for word in words:
            for c in word:
                adj[c] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            minLen = min(len(w1), len(w2))
            # in case of 'apes', 'ape' we have invalid dict; prefix must come first
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # not in visit, never visited. True, currently exploring. False, fully explored
        res = []

        # post order dfs for topo sort
        def dfs(c):
            if c in visit: # if c is actively being explored and found again, cycle
                return visit[c]

            visit[c] = True

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c): # bubble up found cycle
                return ""

        # topo sort returns reversed order
        res.reverse()
        return "".join(res)