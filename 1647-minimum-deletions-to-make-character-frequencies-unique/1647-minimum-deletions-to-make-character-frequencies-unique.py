class Solution:
    def minDeletions(self, s: str) -> int:
        char_freq= Counter(s)
        seen_freq = set()
        answer = 0

        for cnt in char_freq.values():
            while cnt in seen_freq:
                cnt -= 1
                answer += 1

            if cnt:
                seen_freq.add(cnt)

        return answer