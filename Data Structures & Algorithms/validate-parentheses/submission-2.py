class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        left = "({["

        for i in range(0, len(s)):
            if s[i] in left:
                if (stack and stack[-1] in left) or (not stack):
                    stack.append(s[i])
                    continue
                return False
            else:
                if stack and stack[-1] in left:
                    if stack[-1] =="(" and s[i]==")":
                        stack.pop()
                    elif stack[-1]=="[" and s[i]=="]":
                        stack.pop()
                    elif stack[-1]=="{" and s[i]=="}":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return stack==[]
                        