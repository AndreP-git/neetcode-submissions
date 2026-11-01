class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        prefix.append(0)
        print(prefix)

        for i in range(1, len(nums)+1):
            right_sum = prefix[-2] - prefix[i] if i < len(prefix)-1 else prefix[-1]
            left_sum = prefix[i-1]
            print(left_sum, right_sum)
            if right_sum == left_sum:
                return i-1
        return -1