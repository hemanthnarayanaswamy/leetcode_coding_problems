class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1, m1, s1 = startTime.split(':')
        h2, m2, s2 = endTime.split(':')
        print(h1, h2, m1, m2, s1, s2)

        t1 = int(h1)*60*60 + int(m1)*60 + int(s1)
        t2 = int(h2)*60*60 + int(m2)*60 + int(s2)

        return abs(t1 - t2)