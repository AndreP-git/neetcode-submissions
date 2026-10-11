class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        n = len(nums) # saving it to decrease its value 

        while i < n:
            if nums[i] == val: # found element to remove
                n -= 1 # decrease tot number of elements "to check", also necessary for first copy!
                nums[i] = nums[n]
            else:
                i += 1 # element is ok, move to next
        
        return n # return number of "valid" remaining elements

