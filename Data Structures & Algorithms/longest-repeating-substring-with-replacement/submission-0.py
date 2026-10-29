class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        counter = {}
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_freq = max(max_freq, counter[s[right]])

            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len        