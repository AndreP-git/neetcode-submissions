class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [nums[0]]
        for num in nums[1:]:
            self.prefix.append(self.prefix[-1] + num)
        print(self.prefix)
 
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - (self.prefix[left-1] if left-1 >= 0 else 0)
        
 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)