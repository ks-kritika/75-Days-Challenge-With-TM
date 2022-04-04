#O(n) Approach
class Solution(object):
    def largestRectangleArea(self, height):
            res = 0
            stack = []
            height = [0] + height + [0]
            for i in range(len(height)):
                while(stack and height[stack[-1]] > height[i]):
                    j = stack.pop()
                    res = max(res, (i-stack[-1]-1)*height[j])
                stack.append(i)
            return res
        

'''
O(N**2) Approach
class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        res=0
        for i in range(len(h)):              #i=4
            l =0
            for j in range(i,-1,-1):   #finding the left smaller element
                if h[j]>=h[i]:         # j=4,3,2,1,0
                    l+=1
                else:
                    break

            for j in range(i+1,len(h)):    #finding the right smaller element
                if h[j]>=h[i]:            #j=5
                    l+=1
                else:
                    break

            res = max(res,l*h[i])
        return res
'''