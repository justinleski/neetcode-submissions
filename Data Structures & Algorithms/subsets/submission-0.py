class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(index, curr, ans):

            if index == n:
                # capture snapshot of current state
                ans.append(curr.copy())
                return curr

            # make decision to do nothing, or add from nums
            temp = nums[index] # has to be stored here otherwise indexo out of bounds

            # the do nothing
            index += 1
            dfs(index, curr, ans)

            # the do something
            # temp = nums.pop() # ISSUE -> fuck
            curr.append(temp)
            dfs(index, curr, ans)
            curr.remove(temp)


        # START MAIN
        n = len(nums)
        curr = []
        ans = []

        dfs(0, curr, ans)

        return ans
            
