class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        # we can use bfs and try out every combination and store it in the result.
        
        res = []

        # create mapping of the numbers = 2 = ["a", "b", "c"]
        # 3 = "def"
        if not digits:
            return []
        
        dict_phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        

        def dfs(index, temp):
            if index==len(digits):
                res.append("".join(temp[:]))
                return 
            # print(digits[index], index)
            for char in dict_phone[digits[index]]:
                temp.append(char)
                dfs(index+1, temp[:])
                temp.pop()
            return 
        
        dfs(0, [])
                    
                
            
            

        return res
