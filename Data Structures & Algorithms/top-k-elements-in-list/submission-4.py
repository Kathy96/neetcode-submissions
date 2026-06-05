class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, cnt in count.items():
            freq[cnt].append(n)
        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for j in freq[i]:
                    res.append(j)
                    k -= 1
                    if k == 0:
                        return res
                