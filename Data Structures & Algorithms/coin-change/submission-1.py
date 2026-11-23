class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if not coins:
            return -1
        elif amount == 0:
            return 0

        dp = [None] * (amount + 1)
        dp[0] = 0


        def memo(curr):

            if curr == 0:
                return 0
            else:
                minVal = float('inf') # min will be 0 in cases of others not being found yet
                for c in coins:

                    if curr - c >= 0:
                        if dp[curr - c] is not None:
                            child = dp[curr - c]
                        else:
                            child = memo(curr - c)

                        if minVal > child:
                            minVal = child
                dp[curr] = 1 + minVal
                return dp[curr]

            # for c in coins:
            #     if curr - c >= 0:
            #         dp[c] = memo(curr - c)
               

        val = memo(amount)
        if not val or val == float('inf'):
            return -1

        return val
        # print(dp)
        # return dp[amount]


        # count = 0
        # coins.sort(reverse=True) # coins not assumed ot be sorted

        # dp = [None] * len(coins)


        # # coins sorted descending for value
        # for i, c in enumerate(coins):

        #     # we can add the same coin multiple times
        #     while c <= amount:
        #         dp[i] += 1

            










      