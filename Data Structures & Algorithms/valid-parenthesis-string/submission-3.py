class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []

        for i in range(0, len(s)):
            if s[i]=="(":
                opens.append(i)
            elif s[i]=="*":
                stars.append(i)
            else:
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while opens and stars:
            if opens.pop()>stars.pop():
                return False
        return not opens

