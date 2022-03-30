class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs_backtrack(i,curr,total):
            if i>=len(candidates) or total> target :
                return
            if total==target:
                res.append(curr[:])
                return 
            
            curr.append(candidates[i])
            dfs_backtrack(i,curr,total+candidates[i])
            curr.pop()
            dfs_backtrack(i+1,curr,total) 


        dfs_backtrack(0,[],0)
        return res