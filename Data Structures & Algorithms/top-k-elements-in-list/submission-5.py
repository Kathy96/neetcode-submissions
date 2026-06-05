class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i, n in count.items():
            freq[n].append(i)
        for i in range(len(nums), -1 , -1):
            if freq[i]:
                for n in freq[i]:
                    res.append(n)
                    k -= 1
                    if k == 0:
                        return res
