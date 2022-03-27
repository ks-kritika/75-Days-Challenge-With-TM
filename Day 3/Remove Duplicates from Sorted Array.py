class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list1  = []
        for i in nums:
            if i not in list1:
                list1.append(i)
                
        nums.clear()
        
        for i in list1:
            nums.append(i)
        return len(nums)