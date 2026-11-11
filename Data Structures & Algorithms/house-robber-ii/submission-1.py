class Solution:
    def rob(self, nums: List[int]) -> int:
        lenNums = len(nums)

        if not nums:
            return 0
        elif lenNums == 1: # no neighbours to alert
            return nums[0]
        elif lenNums <= 3:
            return max(nums)


        # exclude last house
        back2 = nums[0]
        back1 = max(nums[0], nums[1])

        for i in range(2, lenNums - 1):
            # i realized we dont need to update the array
            temp = max(back1, nums[i] + back2) 

            back2 = back1
            back1 = temp


        # exclude first house
        secondBack2 = nums[1]
        secondBack1 = max(nums[1], nums[2])

        for i in range(3, lenNums):
            temp = max(secondBack1, nums[i] + secondBack2) 

            secondBack2 = secondBack1
            secondBack1 = temp

        return max(back1,back2,secondBack2,secondBack1)


        # back2 = nums[0]
        # back1 = None
        # beginRobbed = True

        # # flag to tell us if first house robbed, so on last we can check if neighbors
        # if(nums[0] > nums[1]):
        #     back1 = nums[0]
           
        # else:
        #     back1 = nums[1]
        #     beginRobbed = False


        # for i in range(2, len(nums)):

        #     nums[i] = max(back1, nums[i] + back2)

        #     back2 = back1
        #     back1 = nums[i]

        # print(beginRobbed)
        # if beginRobbed:
        #     return back2
        # else:
        #     return back1