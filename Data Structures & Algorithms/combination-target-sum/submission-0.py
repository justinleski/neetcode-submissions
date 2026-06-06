class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        results = []

        def dfs(index, curr, remaining):

            if remaining == 0:
                results.append(curr.copy())
                return

            if remaining < 0 or index >= len(nums):
               return

            #for i in range(len(candidates)):# stupid dont do this for dfs
            candidate = nums[index]
            curr.append(candidate)
            dfs(index, curr, remaining - candidate) # remove from our running total
            curr.pop()
            dfs(index+1, curr, remaining)

        # MAIN call
        dfs(0, [], target)
        return results