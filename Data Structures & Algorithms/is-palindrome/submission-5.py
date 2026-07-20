class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(char.lower() for char in s if char.isalnum()) # is alnum removes punctuation
        # print(s)
        # print(len(s))

        # edge case
        if (len(s) <= 1): # we can use this to indicate punctuation stripepd as constraints say 1<=s
            return True
        
        # assume O(n), two poitner soln
        l = 0
        r = len(s) - 1

        while (s[l] == s[r]):
            if (l >= r):
                return True

            l += 1
            r -= 1

        return False

       