class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # since a permutation: aab -> aab, aba, baa is size of o.g. string
        if len(s1) > len(s2):
            return False

        # how do we know if all current characters are not in?

        inWindow = [0] * 26 # each alphabet character counted in here - index via ord(char) - ord('a')
        inPerm = [0] * 26

        for i in range(len(s1)):
            inPerm[ord(s1[i]) - ord('a')] += 1
            inWindow[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if (inPerm[i] == inWindow[i]):
                matches += 1
            
        l = 0 # left ptr moves as lower bound
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            inWindow[index] += 1

            if inPerm[index] == inWindow[index]:
                matches += 1
            elif inPerm[index] + 1 == inWindow[index]:
                matches -= 1

            # l
            index = ord(s2[l]) - ord('a')
            inWindow[index] -= 1
            l += 1

            if inPerm[index] == inWindow[index]:
                matches += 1
            elif inPerm[index] - 1 == inWindow[index]:
                matches -= 1

        return matches == 26


        # # scan s2 for perms of s1 - kind of like anagram
        # for r, char in enumerate(s2):

        #     # once we have window, we need to somehow check if counts equal
        #     if inPerm[ord(char) - ord('a')] != inWindow[ord(char) - ord('a')]:
        #         diff -= 1

        #     inWindow[ord(char) - ord('a')] += 1

        #     # once we have window, we need to somehow check if counts equal
        #     if inPerm[ord(char) - ord('a')] != inWindow[ord(char) - ord('a')]:
        #         diff += 1



  
        #     if inPerm[ord(char) - ord('a')] != inWindow[ord(char) - ord('a')]:
        #         diff -= 1

        #     # our window will be as big as s1 - size of our perms
        #     if r - l >= len(s1):
        #         inWindow[ord(s2[l]) - ord('a')] -= 1
        #         l += 1

        #     if inPerm[ord(char) - ord('a')] != inWindow[ord(char) - ord('a')]:
        #         diff += 1

   
      

            
        #     print(inWindow)
        #     print(inPerm)
        #     print(char)
        #     print(diff)
        #     print(r - l)
        #     print()
        #     print()

        #     # finally - make sure + 1
        #     if diff == 26 and r - l + 1 == len(s1):
        #         return True


        # # no matches found
        # return False