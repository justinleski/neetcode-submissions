class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # not most efficient - trying 2D DP approach
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxLen = 0
        startIndex = 0

        for length in range(1, n + 1):


            # try every substring in range of len
            for i in range(0, n - length + 1):
                j = i + length - 1

                # base case, all strs of len 1 are palindromes
                if length == 1 or (length == 2 and s[i] == s[j]):
                    dp[i][j] = True
                    maxLen = length
                    startIndex = i
                    continue
                # elif j+1 >= length:# out of bounds
                #     continue
                elif dp[i+1][j-1] == True and s[i] == s[j]:
                    dp[i][j] = True
                    maxLen = length
                    startIndex = i
                    continue
                
                dp[i][j] = False


        # print(s[startIndex:(startIndex + maxLen)])
        return s[startIndex:(startIndex + maxLen)]