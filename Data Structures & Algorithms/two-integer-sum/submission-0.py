class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [target - num, idx]
        seen = {}

        for idx, num in enumerate(nums):
            if num in seen:
                return [seen[num], idx]
            else:
                seen[target - num] = idx
        