class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        if not cost:
            return 0
        if len(cost) <= 2:
            return min(cost)
        #elif len(cost) == 3:
            #return min(cost[0]+cost[2], cost[1])
            
        
        #dp = [0] * len(cost)
        #currStep = 1
        cost.append(0) # top can be imsgined as extra stsir w no cost
        
        back1 = cost[0]
        back2 = cost[1]
        minCost = 0
        for i in range(2,len(cost)):
            minCost = cost[i] + min(back1,back2)
            
            back1 = back2
            back2 = minCost
            
        
        
        return minCost
        
            
            
            