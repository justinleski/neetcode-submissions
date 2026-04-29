class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sliding window's are always two pointers, but two pointers not always sliding window
        l = 0 
        r = 1
        maxDiff = 0

        # in sliding window, both left and right move forward
        for i,p in enumerate(prices):

            diff = prices[i] - prices[l]

            if prices[i] < prices[l]:
                l = i 
            elif diff > maxDiff:
                r = i
                maxDiff = diff

        #print(maxDiff)
        return maxDiff
