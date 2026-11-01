class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for i in range(len(nums)):
            right_sum = prefix[len(nums)] - prefix[i+1]
            left_sum = prefix[i]
            if right_sum == left_sum:
                return i
        return -1