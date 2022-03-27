class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt={}
        
        for i in range(len(nums)):
            number = nums[i]
            required = target - number
            
            if required in dt:
                return [dt[required],i]
            else:
                dt[number]=i