class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        friendsFreq = {i: 0 for i in range(n)}
        count = 1
        i = 0

        while i in friendsFreq:
            friendsFreq[i] += 1
            if friendsFreq[i] == 2:
                break
            dist = count * k
            i = (i + dist) % n
            count += 1
        
        return [p+1 for p in range(n) if not friendsFreq[p]]