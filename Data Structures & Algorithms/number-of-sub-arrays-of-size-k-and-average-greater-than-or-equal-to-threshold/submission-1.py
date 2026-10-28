class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # [1,2,3,3,2,5,1] k=3 threshold=3
        # [1,2,3] --> avg: 6/3=2 --> 2 > 3 ? no
        # [2,3,3] --> avg: 8/3=2.6 --> 2.6 > 3 ? no
        # 3,2,5 --> avg: 3.3 --> yes --> count + 1

        left = 0
        count = 0
        curr_sum = 0

        for right in range(len(arr)):
            curr_sum += arr[right]
            if right - left + 1 > k:
                curr_sum -= arr[left]
                left += 1
            if right - left + 1 == k:
                count += 1 if curr_sum >= threshold * k else 0
        
        return count

