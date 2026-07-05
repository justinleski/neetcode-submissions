class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # convert str to arr for easier ops
        # arr = list(s)
        curr = []
        ans = []

        def isValidPalindrome(s: str, i: int, j: int) -> bool:
            # Take susbtr and check if it is palindrome
            lPtr = i
            rPtr = j

            while (lPtr < rPtr):
                if (s[lPtr] != s[rPtr]):
                    return False
                lPtr += 1
                rPtr -= 1

            return True

        def backtrack(index: int):
            if (index == len(s)):
                ans.append(curr.copy())

            # how do we build a string here
            for j in range(index, len(s)):
                if isValidPalindrome(s, index, j):
                    curr.append(s[index: j + 1])
                    backtrack(j + 1)

                    # back track
                    curr.pop()
                    # backtrack(index - 1)


            # curr.append(s[index])
            # backtrack(index + 1)

        # MAIN
        backtrack(0)
        return ans