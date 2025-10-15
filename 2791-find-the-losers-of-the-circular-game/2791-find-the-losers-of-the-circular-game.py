class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        friendsFreq = {i: 0 for i in range(n)}
        count = 1
        idx = 0

        while idx in friendsFreq:
            friendsFreq[idx] += 1
            if friendsFreq[idx] == 2:
                break
            dist = count * k
            idx = (idx + dist) % n
            count += 1
        
        return [i+1 for i in range(n) if not friendsFreq[i]]