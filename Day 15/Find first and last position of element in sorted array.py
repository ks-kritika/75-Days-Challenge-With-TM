class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        final_ans=[]
        if target not in nums:
            final_ans.append(-1)
            final_ans.append(-1)
        else:
            ans=[]
            j=0
            for i in nums:
                if i==target:
                    ans.append(j)
                j+=1
            final_ans.append(ans[0])  #first occurence
            final_ans.append(ans[-1]) #last occurrence
        return(final_ans)