class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                r += 1
                l += 1
            else:
                r += 1
        
        while l < len(nums):
            nums[l] = 0
            l += 1