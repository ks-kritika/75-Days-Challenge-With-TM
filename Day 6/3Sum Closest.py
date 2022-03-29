class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
            n=len(nums)
            nums=sorted(nums)

            minDiff=10000
            minSum = sum(nums[:3])

            for i in range(n-1):
                lower = i + 1
                upper = n - 1
                while lower < upper:
                        current_sum = (nums[i] + nums[lower] + nums[upper])

                        if current_sum > target:
                            upper -= 1

                        elif current_sum < target:
                            lower += 1

                        else:
                            return(current_sum)

                        if minDiff > abs(current_sum-target):
                            minDiff = abs(current_sum-target)
                            minSum = current_sum

            return(minSum)    