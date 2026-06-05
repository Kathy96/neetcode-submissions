class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if len(count) <= 2:
                continue
            keys = list(count.keys())
            for k in keys:
                count[k] -= 1
                if count[k] == 0:
                    del count[k]
        
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res