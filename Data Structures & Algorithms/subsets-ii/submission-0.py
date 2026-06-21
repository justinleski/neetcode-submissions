class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort() # to skip dupes -> O(n logn)

        def dfs(curr, index):
            print(curr)

            if (index == len(nums)):
                result.append(curr.copy())
                return

            curr.append(nums[index])
            dfs(curr, index + 1)

            # back tracking step - go back, check if current number see NOW
            # the reason the while loop is here because a subset can have duplicates
            # but the order doesnt matter. so it's been done once, then we don't need to again
            curr.pop()
            while(index < len(nums) -1  and nums[index] == nums[index + 1]):
                index += 1
            dfs(curr, index + 1)

        #MAIN
        dfs([],0)
        return result