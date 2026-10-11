class Solution:
    def trap(self, height: List[int]) -> int:
        
        # no rain water can be trapped if we only have 1-2 entries
        if len(height) <= 2:
            return 0

        l = 0
        r = len(height) - 1
        area = 0

        lMax = height[l]
        rMax = height[r]

        while (l < r):

            while (lMax < rMax and l < r):
                if lMax < height[l]:
                    lMax = height[l]
                else:
                    area += min(lMax, rMax) - height[l] 
                l += 1

            while (lMax >= rMax and l < r):
                if rMax < height[r]:
                    rMax = height[r]
                else:
                    area += min(lMax, rMax) - height[r] 
                r -= 1

        # max(0,...) in casesd we have no traps, so we can have negative rainwater
        if l == r:
            area += max(0, min(lMax, rMax) - height[l])

        return area

        # i think it's while loop with iteration in between? wait no
        # while r < len(height):

        #     for ():
        #         continue


        # # is this not technically sliding window?
        # for i, h in enumerate(height):

        #     area = min(height[l], height[r]) * i

           

        #     if (area == 0 and ):


        