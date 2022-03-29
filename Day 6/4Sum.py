class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quad = []
        nums=sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                lower = j+1
                upper = len(nums) - 1
                while lower < upper:
                    s = (nums[i] + nums[j] + nums[lower] + nums[upper])
                    if s == target:
                        quad.append((nums[i], nums[j],nums[lower], nums[upper]))
                        lower += 1
                    elif s < target:
                        lower += 1
                    else:
                        upper -=1

        return(list(set(quad)))