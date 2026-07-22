class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # numbers is increasing
        l = 0
        r = len(numbers) - 1 # return 1-indexed though?

        while (l < r):
            sum = numbers[l] + numbers[r]

            if (sum == target):
                # assume 1-indexed array, so return indices
                return [l+1, r+1]

            # We cannot have a sum of two positive integers where one is greater than the designated sum
            elif (sum > target):
                r -= 1

            elif (sum < target):
                l += 1

        # if we don't find two numbers to sum to target, return empty array
        return []

