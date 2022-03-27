class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st=""
        for i in digits:
            st+=str(i)
        num=int(st)
        num+=1
        res=list(str(num))
        
        return res