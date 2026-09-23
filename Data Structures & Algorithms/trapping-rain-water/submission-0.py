class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        r = len(height) - 1 
        l = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                result += max(leftMax, height[l]) - height[l]
                leftMax = max(leftMax, height[l])
            else: 
                r -= 1
                result += max(rightMax, height[r]) - height[r]
                rightMax = max(rightMax, height[r])

        

        return result
        