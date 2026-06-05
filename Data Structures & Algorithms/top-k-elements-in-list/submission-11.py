class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        {1:1, 2:2, 3:3}
        """
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        bucket = [[] for i in range(len(nums)+1)]
        """
         0.  1.  2.  3.  4.   5.  6
        [[], [], [], [], [], [], []]
        """
        for n, c in count.items():
            bucket[c].append(n)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


        