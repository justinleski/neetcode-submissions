class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        curr = ['('] # since ')' would imemdiatley fail, start here - string immutable so use array
        
        def dfs(open, closed):
            # print(curr)
            # if we have more opening brackets than half the depth of the tree, impossible to close
            if (open > n):
                # curr.pop()
                # open -= 1
                return

            if (closed > open):
                return

            if (len(curr) >= 2*n): # since we can have a max of 2*n brackets
                result.append("".join(curr)) # turn array into string
                return

            curr.append('(')
            open += 1
            dfs(open, closed)
            curr.pop()
            open -= 1

            curr.append(')') 
            closed += 1
            dfs(open, closed)
            curr.pop()
            closed -= 1

            # we want to undo our decision?
            # temp = curr.pop()
            # if (temp == '('):
            #     open -= 1
            # else:
            #     closed -= 1

        #MAIN
        dfs(open = 1, closed = 0)
        #print(result)
        return result