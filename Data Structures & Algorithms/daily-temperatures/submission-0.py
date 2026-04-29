class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                top = stack.pop()
                result[top[1]] = i - top[1] # idx 1 is the index value
            
            
            stack.append((temp, i))

            # # Current idx minus lesser values index
            # if stack:
               
            # else:
            #     result[i] = 0

        # print(result)
        return result
            