class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]
        for n in nums:
            newPerm = []
            for p in perm:
                for i in range(len(p) + 1):
                   p_copy = p.copy()
                   p_copy.insert(i, n)
                   newPerm.append(p_copy)
            perm = newPerm
        return perm 