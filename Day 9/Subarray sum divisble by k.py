class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dt={0:1}
        prefix_sum = 0
        res = 0
        
        for i in nums:
            prefix_sum+=i
            rem = prefix_sum % k
            
            if rem in dt:
                res += dt[rem]
                dt[rem]+=1
            else:
                dt[rem] = 1
                
        return res