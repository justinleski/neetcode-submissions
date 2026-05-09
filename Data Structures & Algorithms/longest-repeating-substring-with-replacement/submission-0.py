class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charFreq = {}
        maxFreq = 0
        l = 0

        for i, r in enumerate(s):
            charFreq[r] = 1 + charFreq.get(r, 0)

            while (i - l + 1) - max(charFreq.values()) > k:
                charFreq[s[l]] -= 1
                l += 1

            maxFreq = max(maxFreq, i - l + 1)

        return maxFreq