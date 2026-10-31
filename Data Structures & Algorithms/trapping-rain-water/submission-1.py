class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        tot_water = 0

        for right in range(len(height)):
            if height[right] >= height[left]:
                curr = left
                while curr < right:
                    tot_water += min(height[left], height[right]) - height[curr]
                    curr += 1
                left = right
        
        right = len(height)-1
        for left in range(len(height)-1, -1, -1):
            if height[left] > height[right]:
                curr = right
                while curr > left:
                    tot_water += min(height[left], height[right]) - height[curr]
                    curr -= 1
                right = left

        return tot_water

