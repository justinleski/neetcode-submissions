class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        currMax = 0

        # pointer
        l = 0

        # right pointer constantly going
        for r, char in enumerate(s):

            while char in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])

            # find maxima
            currMax = max(currMax, r - l + 1)


        return currMax






        # # dict to store seen chars
        # charDict = dict.fromkeys(s, 0)
        # candidates = []


        # # l and r indices (bounds)
        # l = 0
        # r = 1

        # # our current i in the loop can be our "explorer"
        # for i, char in enumerate(s):

        #     print("-------")
        #     print("l is "+str(l))
        #     print("r is "+str(r))
        #     print("i is "+str(i))

        #     charDict[char] += 1
            
        #     if r == l and s[r] != s[l]:
        #         #r = i
        #         continue
        #     elif char != s[r] and charDict[char] == 0:
        #         r = i

        #     # if we find the count of characters means repeats, save indices and move on
        #     else:

        #         # save
        #         candidates.append( r - l + 1 ) # +1 since offset of 1 by 0-index

        #         # clear dict
        #         charDict = {k: 0 for k in charDict} # set all entries to 0

        #         # move on
        #         l = r = i


        # return max(candidates)

