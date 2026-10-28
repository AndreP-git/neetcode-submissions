class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # [1,2,3,1] k=3
        # [1,2,3,1]
        # set = (1,2,3,) -- true

        # [1,2,3,1,5,1] k =2
        # [1,2,3]
        # [2,3,1]
        # [3,1,5]
        # [1,5,1]

        l = 0
        seen = set()
        
        for r in range(len(nums)):
            if r - l == k+1:
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True
            else:
                seen.add(nums[r])

        return False