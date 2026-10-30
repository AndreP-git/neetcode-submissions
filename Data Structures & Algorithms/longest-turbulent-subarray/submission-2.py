class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        left, right = 0, 1
        max_len = 1
        prev = ""

        while right < len(arr):
            if arr[right-1] > arr[right] and prev != ">":
                max_len = max(max_len, right - left + 1)
                prev = ">"
                right += 1
            elif arr[right-1] < arr[right] and prev != "<":
                max_len = max(max_len, right - left + 1)
                prev = "<"
                right += 1
            else:
                right += 1 if arr[right] == arr[right-1] else 0
                left = right - 1
                prev = ""
        
        return max_len