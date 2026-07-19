class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        curr = []
        ans = []

        nums = {
            '2': ["a", "b", "c"], 
            '3': ["d", "e", "f"], 
            '4': ["g", "h", "i"], 
            '5': ["j", "k", "l"], 
            '6': ["m", "n", "o"], 
            '7': ["p", "q", "r", "s"], 
            '8': ["t", "u", "v"], 
            '9': ["w", "x", "y", "z"]
        }

        def dfs(digitsIndex):

            if(digitsIndex == len(digits)):
                ans.append(''.join(curr))
                return

            for digit in nums[digits[digitsIndex]]:
                curr.append(digit)
                #print(curr)
                dfs(digitsIndex + 1)
                curr.pop()

        # MAIN
        if len(digits) == 0:
            return ans
        dfs(0)
        return ans


# def dfs(digitsIndex, letterIndex):

#             if(digitsIndex == len(digits)):
#                 ans.append(''.join(curr))
#                 return



#             # explore all letters of a digit
#             # if (letterIndex < len(nums[digitIndex][letterIndex])):

#             curr.append(nums[digits[digitsIndex]][letterIndex])
#             print(curr)
#             dfs(digitsIndex + 1, letterIndex)

#             # after we hit base case we und up here
#             # let's remove a letter we just did and try a new letter on same digit
#             # dont forget to remove the last letter you put
#             curr.pop()
#             if letterIndex < len(nums[digits[digitsIndex]]):
#                 dfs(digitsIndex, letterIndex + 1)
#             else:
#                 curr.pop()
#                 dfs(digitsIndex + 1, 0)



#             #dfs(digitsIndex + 1, letterIndex)