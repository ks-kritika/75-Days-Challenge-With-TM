class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        currSum = 0                 #initializing 0 to a count of 1 because an empty subarray still counts as 1
        dic = {0:1}
        for n in nums:
            currSum += n
            diff = currSum - k

            if diff in dic:
                res += dic[diff]
            
            if currSum not in dic:
                dic[currSum] = 0
            dic[currSum] += 1
           
            
        return res