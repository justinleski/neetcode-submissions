class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [0] * len(nums)
        temp = 1
        zeroIndex = -1
        zeroCount = 0

        # producto of everything
        for i, num in enumerate(nums):
            if num == 0:
                zeroIndex = i
                zeroCount += 1
                if zeroCount > 1:
                    return output # since our array of 0s hass not been modified yet
            else:
                temp = temp * num

        if zeroCount == 1:
            output[zeroIndex] = temp
            return output # since all other indices are 0

        # we can just divide out each entry to make product except self - assumes no 0
        for i, num in enumerate(nums):
            output[i] = int(temp / num)

        return output