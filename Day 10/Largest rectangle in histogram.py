class Solution(object):
    def largestRectangleArea(self, height):
            ans = 0
            stack = []
            height = [0] + height + [0]
            for i in range(len(height)):
                while(stack and height[stack[-1]] > height[i]):
                    j = stack.pop()
                    ans = max(ans, (i-stack[-1]-1)*height[j])
                stack.append(i)
            return ans
        