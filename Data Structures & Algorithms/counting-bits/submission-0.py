class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0 for _ in range(n + 1)]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            arr[i] = arr[i - offset] + 1
        return arr
