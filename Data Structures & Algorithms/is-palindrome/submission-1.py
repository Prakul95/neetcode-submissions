class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            while l<r and (s[l]==" " or not self.isalphaCheck(s[l])):
                l+=1
            while r>l and (s[r]==" " or not self.isalphaCheck(s[r])):
                r-=1
            if  s[l].lower()==s[r].lower():
                r-=1
                l+=1
            else:
                return False
        return True
        
    def isalphaCheck(self,c):

        return (ord("A")<=ord(c)<=ord("Z") or ord("a")<=ord(c)<=ord("z") or ord("0")<=ord(c)<=ord("9"))


            