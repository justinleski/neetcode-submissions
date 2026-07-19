class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # technically O(1) since alphabet fixed O(26), array would be more space efficient
        sHash = Counter(s)
        tHash = Counter(t)

        if sHash == tHash:
            return True

        return False

