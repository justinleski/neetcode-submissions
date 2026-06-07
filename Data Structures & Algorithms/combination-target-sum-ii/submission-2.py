class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidatesLen = len(candidates) - 1

        def dfs(index, curr, currSum):
            # currSum = sum(curr) # recalculating sum is not efficient

            if(currSum == target):
                #if (curr not in ans): #NOPE, because we try path then reject, should reject before trying to minimize time
                ans.append(curr.copy())
                return
            # out of bounds we stop ()
            if(currSum > target or (index > candidatesLen)):
                return

            # append
            curr.append(candidates[index])
            currSum += candidates[index]
            dfs(index + 1, curr, currSum)

            #pop / back track
            popped = curr.pop() # reverse last step
            currSum -= popped
            # if our next number(s) is the same, do not try the path again sicne we know the outcome
            while (not (index + 1 > candidatesLen) and popped == candidates[index + 1]):
                index += 1

            dfs(index + 1, curr, currSum)

        #MAIN
        candidates.sort() # sorting helps us skip dupicates w/o hash set
        dfs(0, [], 0)
        return ans



         # def dfs(index, visited, curr):
        #     print(index)

        #     if(sum(curr) == target):
        #         ans.append(curr.copy())
        #         return
        #     if(sum(curr) > target):
        #         return

        #     print("test")

        #     # append       
        #     # visited.append(index) # refers to index in candidates
        #     curr.append(candidates[index])
        #     for i in range(len(candidates)):
        #         if candidates[index] in visited:
        #             index += 1
        #         else:
        #             break
        #     dfs(index, visited, curr) # TODO: skip indexes until not visited

        #     #pop      
        #     popped = curr.pop()
        #     for i in range(len(candidates)):
        #         if candidates[index] in visited:
        #             index += 1
        #         else:
        #             break
        #     dfs(index, visited, curr) # TODO: skip indexes until not visited