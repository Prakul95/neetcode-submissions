class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def check_pal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        res = []
        def dfs(index, temp):
            if index>=len(s):
                res.append(temp[:])
                return
            for i in range(index, len(s)):
                if check_pal(index, i):
                    temp.append(s[index:i+1])
                    dfs(i+1, temp[:])
                    temp.pop()
            return 
        dfs(0, [])
        return res

