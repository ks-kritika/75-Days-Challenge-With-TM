class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dt={}
        for i in nums:
            if i not in dt:
                dt[i]=1
            else:
                dt[i]+=1
                
        ans=[]
        for i in dt:
            if dt[i]>1:
                ans.append(i)
        return ans