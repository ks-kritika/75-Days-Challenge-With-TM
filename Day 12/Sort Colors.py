class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z,o,t=0,0,0
        for i in nums:
            if i==0:
                z+=1
            elif i==1:
                o+=1
            else:
                t+=1
        for i in range(z + o + t):
            if i < z:
                nums[i] = 0
            if i >= z and i < z + o:
                nums[i] = 1
            if i >= z +o and i < z + o + t:
                nums[i]  = 2
        