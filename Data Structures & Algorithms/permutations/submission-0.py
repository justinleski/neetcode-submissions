class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # maintain ans
        ans = []
        n = len(nums)
        chosen = [False] * n # instead of hash map take advantage of indexes we maintain

        def dfs(curr):

            print(curr)

            # only one case since we need n items in array: n! answers
            if (len(curr) == n):
                ans.append(curr.copy())
                return

            for i in range(n):
                if chosen[i] == True:
                    continue

                curr.append(nums[i])
                chosen[i] = True

                dfs(curr)

                # back track
                curr.pop()
                chosen[i] = False

        # MAIN
        dfs([])
        return ans 
                
        # def dfs(index, curr)
            # # back track
            # if (chosen[index] == False):
            #     curr.append(nums[index])
            #     chosen[index] = True # set as seen/chosen

            # while (index < n and chosen[index] == True):
            #     index += 1
            # dfs(index, curr)

       
            # curr.pop()
            # # prevIndex = index
            # index -= 1
            # chosen[index] = False # once
            # dfs(index, curr)
           


        