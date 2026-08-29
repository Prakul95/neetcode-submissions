class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(temp, curr, index):
            
            
            if curr==target:
                res.append(temp[:])
                return 

            
            for i in range(index, len(candidates)):

                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if curr+candidates[i]>target:
                    break
                temp.append(candidates[i])
                dfs(temp[:], curr+candidates[i],i+1)
                temp.pop()
            return 
        dfs([],0,0)

        return res


            
