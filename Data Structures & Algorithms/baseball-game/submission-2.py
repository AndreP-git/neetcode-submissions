class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        curr_sum = 0

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
                curr_sum += stack[-1] + stack[-2]
            elif op == "D":
                stack.append(stack[-1] * 2)
                curr_sum += stack[-1] * 2
            elif op == "C":
                curr_sum -= stack.pop()
                
            else:
                stack.append(int(op))
                curr_sum += int(op)

        return sum(stack)