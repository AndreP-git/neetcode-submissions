class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for idx, a in enumerate(nums):
            if a > 0: # if the smallest element is positive, it's impossible to have a+b+c == 0
                break
            
            if idx > 0 and a == nums[idx-1]:
                continue
            
            left, right = idx+1, len(nums)-1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
            
        return res