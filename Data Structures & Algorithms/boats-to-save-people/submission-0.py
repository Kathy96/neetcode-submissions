class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r, res = 0, len(people) - 1, 0
        people.sort()
        while l <= r:
            remain = limit - people[r]
            if remain >= people[l]:
                l += 1
            r -= 1
            res += 1
        return res