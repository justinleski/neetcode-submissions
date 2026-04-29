class Solution:

    def encode(self, strs: List[str]) -> str:

        string = "" # O(M chars in num and N strlens appended)

        for word in strs: # iterate through all O(N) strings
            string += (str(len(word)) + "#") # following the hint, use # as delimeter
            string += (word)

        # print(string)
        return string

    def decode(self, s: str) -> List[str]:

        pos = 0
        arr = []

        # we know first char will be len of string, i.e: 4#xxxx
        # this means we also know the end pos
 
        while (pos < len(s)):

            # we need to find what our str length is
            curr = pos
            currBuffer = ""
            while (s[curr] != '#'):
                currBuffer += s[curr]
                curr += 1



            currLen = int(currBuffer)
            start = curr + 1 # curr is left at #, but we need to move it to starting pos which is 1 after

            end = currLen + start - 1 # -1 since we would overcount otherwise

            arr.append(s[start:end+1]) # add 1 specifically for splicing since it is not inclusive of variable "end"

            # now that we have the word appended, our new start should be from old end
            pos = end + 1

        return arr