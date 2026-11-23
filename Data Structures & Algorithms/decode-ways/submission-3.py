class Solution:
    def numDecodings(self, s: str) -> int:


        if not s or s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1

        # dp counts
        back2 = 1 
        back1 = 1
       

        for i in range(1, len(s)):
            curr = 0

            # count individual letters
            if 1 <= int(s[i]) <= 26:
                curr += back1

            # count pairs; join indexes at ptrs like 0 and 1 -> 01
            combined = s[i-1:i+1]
            if 10 <= int(combined) <= 26:
                curr += back2


            back2 = back1
            back1 = curr


        return curr

