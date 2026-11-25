class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1], (nums[0] * nums[1]))

        currMax = nums[0]
        currMin = nums[0]
        maxNo = currMax

        for i in range(1, len(nums)):

            # max contiguous subarray may not be recent, we can maintain that with var instead of dp array
            temp = currMax
            currMax = max(nums[i], currMax * nums[i], currMin * nums[i])
            currMin = min(nums[i], currMin * nums[i], temp * nums[i])

   
            maxNo = max(maxNo, currMax)
           

        return maxNo

        # back2 = nums[0]
        # back1 = nums[0] * nums[1]
        # maxNo = max(back2, back1)


        # for i in range(2, len(nums)):

        #     back2 = back1

        #     # issue is we need code to "restart" on something bad like a -1 followed by pos, or a 0
        #     if back1 <= 0 and nums[i] > 0:
        #         back1 = nums[i]
        #     else:
        #         back1 *= nums[i]

        #     # max contiguous subarray may not be recent, we can maintain that with var instead of dp array
        #     maxNo = max(back2, back1, maxNo)

           
         


        # back2 = nums[0]
        # back1 = nums[0] * nums[1]
        # # dp = [None] * len(nums)
        # maxNo = max(back2, back1)

        # for i in range(2, len(nums)):

        #     #
        #     if nums[i] * back1 > maxNo:
        #         maxNo = nums[i] * back1

        #     elif nums[i] <= 0: # fails to account for the product of two negatives making a positive
        #         back2 = back1
        #         back1 = 1
                

        #     else:
        #         back2 = back1
        #         back1 = back1 * nums[i]




        


   