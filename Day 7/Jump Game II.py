class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        destination = size - 1
        cur_coverage, last_jump_index = 0, 0
        times_of_jump = 0
        if size == 1:
            return 0
        
        for i in range( 0, size):
            cur_coverage = max(i + nums[i], cur_coverage) 
            if i == last_jump_index:
                last_jump_index = cur_coverage
                times_of_jump += 1
                if cur_coverage >= destination:
                        return times_of_jump
                
        return times_of_jump