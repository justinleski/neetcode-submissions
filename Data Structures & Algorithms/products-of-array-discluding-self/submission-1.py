class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #optimize for no division and O(n)
        numLen = len(nums)
        prefix = [1] * numLen
        suffix = [1] * numLen
        output = []

        l = 0
        r = numLen - 1
        lSum = 1
        rSum = 1

        # prefix 
        while l < numLen:
            prefix[l] = lSum
            lSum *= nums[l]
            l += 1

        # suffix
        while r >= 0:
            suffix[r] = rSum
            rSum *= nums[r]
            r -= 1

        # Calculate output
        for i in range(numLen):
            output.append(prefix[i] * suffix[i])

        return output








        # output = [0] * len(nums)
        # temp = 1
        # zeroIndex = -1
        # zeroCount = 0

        # # producto of everything
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         zeroIndex = i
        #         zeroCount += 1
        #         if zeroCount > 1:
        #             return output # since our array of 0s hass not been modified yet
        #     else:
        #         temp = temp * num

        # if zeroCount == 1:
        #     output[zeroIndex] = temp
        #     return output # since all other indices are 0

        # # we can just divide out each entry to make product except self - assumes no 0
        # for i, num in enumerate(nums):
        #     output[i] = int(temp / num)

        # return output