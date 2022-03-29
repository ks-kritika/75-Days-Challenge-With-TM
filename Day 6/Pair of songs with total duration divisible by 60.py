class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:    
        dt = {}
        count = 0
        
        for t in time:
            num = t % 60
            
            if num == 0:
                if 0 in dt:
                    count += dt[0]
            elif (60 - num) in dt:
                count += dt[60 - num]
                
            if num in dt:
                dt[num] += 1
            else:
                dt[num] = 1
                
        return count