class TimeMap:

    def __init__(self):
        # dict = {key: [(timestamp, value)]}
        self.pairs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.pairs:
            self.pairs[key] = [(timestamp, value)]
        else:
            self.pairs[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pairs:
            return ""
        values = self.pairs[key]

        idx = self.search(values, timestamp)
        return values[idx][1] if idx != -1 else ""
    
    def search(self, values: List, timestamp: int) -> int:
        left, right = 0, len(values) - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans