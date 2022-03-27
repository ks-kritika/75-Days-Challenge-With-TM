class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if i!=j and i!=k and j!=k:
                        if nums[i]+nums[j]+nums[k]==0:
                            if (nums[i],nums[j],nums[k]) not in res:
                                res.append((nums[i],nums[j],nums[k]))
        return res