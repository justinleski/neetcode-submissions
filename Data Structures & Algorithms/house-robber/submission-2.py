class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        back2 = nums[0]
        back1 = max(nums[1], nums[0]) # since back1 is max u can rob up to this index, not that index's value


        for i in range(2, len(nums)):

            nums[i] = max(back1, back2 + nums[i])

            # update pointers
            back2 = back1
            back1 = nums[i]



        return nums[len(nums) - 1]

        # even = nums[1]

        # odd = nums[0]

        # for i in range(2, len(nums)):

        #     if i % 2 == 0: # since 0-indexed %2 represents odd
            
        #         odd += nums[i]
        #     else:
        
        #         even += nums[i]


        # return max(even, odd)
