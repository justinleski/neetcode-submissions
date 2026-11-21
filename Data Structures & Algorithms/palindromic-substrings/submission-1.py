class Solution:
    def countSubstrings(self, s: str) -> int:
        
        if not s:
            return 0

        stringLen = len(s)
        total = 0

        if stringLen <= 1:
            return stringLen
        elif stringLen == 2 and s[0] == s[1]:
            return 3

        for i, c in enumerate(s):

            l = i - 1
            r = i + 1
    
            # since single char counts as pal
            total += 1
     
            print(f"{l} and {r}")
            # odd len
            while l >= 0 and r < stringLen and s[l] == s[r]:
          
                l -= 1
                r += 1
                total +=  1

                if l < 0 or r >= stringLen:
                    break
                # if pal is entire string
                # if r == stringLen:
                #     # TODO: not r, since its number of substr
                #     return r

            # even len
            l = i
            r = i + 1

            while l >= 0 and r < stringLen and s[l] == s[r]:
                l -= 1
                r += 1
                total +=  1

                if l < 0 or r >= stringLen:
                    break

        return total




        # # main - expand from center
        # l = 0
        # r = 0

        # if stringLen % 2 == 0:
        #     # even case
        #     r = stringLen // 2
        #     l = r - 1
        # else:
        #     l = stringLen // 2
        #     r = l

        
