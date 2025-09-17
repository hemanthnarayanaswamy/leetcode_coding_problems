class Solution:
    def countPoints(self, rings: str) -> int:
        ringRodMap = defaultdict(set)
        count = set()

        for i in range(0, len(rings), 2):
            c = rings[i]
            r = rings[i+1]
            ringRodMap[r].add(c)

            if len(ringRodMap[r]) == 3:
                count.add(r)

        return len(count)