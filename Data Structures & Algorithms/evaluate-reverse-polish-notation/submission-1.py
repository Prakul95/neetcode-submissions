class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            
            if op =="+":
                a, b = stack.pop(), stack.pop()
                c = a + b
            elif op =="-":
                a, b = stack.pop(), stack.pop()
                c = b-a
            elif op =="*":
                a, b = stack.pop(), stack.pop()
                c = a*b
            elif op =="/":
                a, b = stack.pop(), stack.pop()
                c = int(float(b)/a)
            else:
                c = int(op)
            stack.append(c)
        return stack[0]
                
                