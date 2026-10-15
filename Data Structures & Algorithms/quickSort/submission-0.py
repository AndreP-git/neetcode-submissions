# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs)-1)
    
    def quickSortHelper(self, arr: List[Pairs], s: int, e: int) -> List[Pairs]:
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e].key
        left = s

        for i in range(s, e):
            if arr[i].key < pivot:
                temp = arr[i]
                arr[i] = arr[left]
                arr[left] = temp
                left += 1

        temp = arr[e]
        arr[e] = arr[left]
        arr[left] = temp

        self.quickSortHelper(arr, s, left-1)
        self.quickSortHelper(arr, left+1, e)

        return arr

