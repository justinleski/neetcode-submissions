class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        back1 = 1 # stair 1 has 1 way, and 2 has 2 ways
        back2 = 2


        for i in range(3, n + 1): # not 0 indexed since count
            count = back1 + back2

            back1 = back2
            back2 = count

        return count