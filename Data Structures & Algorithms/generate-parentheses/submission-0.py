class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we can create a dfs and add either a left bracker or right bracket only if left bracket is less than right
        res = []

        def dfs(left, right, temp):

            if left==0 and right ==0:
                res.append("".join(temp[:]))
                return 
            if left>0:
                temp.append("(")
                dfs(left-1, right, temp[:])
                temp.pop()
            
            if right>left:
                temp.append(")")
                dfs(left, right-1, temp[:])
                temp.pop()
                
            return 
        dfs(n,n,[])
        return res
            
            