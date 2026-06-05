# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return
        p = arr[e]
        l = s
        for i in range(s, e):
            if arr[i].key < p.key:
                arr[l], arr[i] = arr[i], arr[l]
                l += 1
        arr[l], arr[e] = arr[e], arr[l]
        self.quickSortHelper(arr, s, l - 1)
        self.quickSortHelper(arr, l + 1, e)
        