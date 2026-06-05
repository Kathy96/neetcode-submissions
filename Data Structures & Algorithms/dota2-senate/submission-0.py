class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        while D and R:
            firstR = R.popleft()
            firstD = D.popleft()
            if firstR < firstD:
                R.append(firstD + n)
            else:
                D.append(firstR + n)


        return "Radiant" if R else "Dire"