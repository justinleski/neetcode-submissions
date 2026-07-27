class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #nlogn

        # if sorted, and leftmost is pos, then no sum will equal 0 - dont have to check len since assumed to be min 3
        if (nums[0] > 0):
            return []

        # l = 0
        # r = len(nums) - 1
        ans = []

        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            # efficient dupe skip oops
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                sum = nums[i] + nums[l] + nums[r] 

                if (sum > 0):
                    r -= 1
                elif (sum < 0):
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]]) 
                    l += 1
                    r -= 1

                    # skip dupes
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return ans





        # nums.sort()
        # print(nums)
        # outputArr = []

        # # if sorted, and leftmost is pos, then no sum will equal 0 - dont have to check len since assumed to be min 3
        # if (nums[0] > 0):
        #     return []

        # l = 0
        # r = len(nums) - 1 

        # while l < r:
        #     pSum = nums[l] + nums[r]

        #     # if sum neg, then move r pointer since it's in pos
        #     if pSum <= 0:
        #         check = pSum + nums[r-1]

        #         if check != 0:
        #             l += 1
        #             # this line will skip any duplictaes of the same number at a diff index
        
        #         else:
        #             outputArr.append([nums[l], nums[r], nums[r-1]])
        #             l += 1
     
        #             r -= 1
            


        #     elif pSum > 0:
        #         check = pSum + nums[l+1]

        #         if check != 0:
        #             r -= 1
          
        #         else:
        #             outputArr.append([nums[l], nums[r], nums[l+1]])
        #             l += 1
                  
        #             r -= 1
               

        # return outputArr