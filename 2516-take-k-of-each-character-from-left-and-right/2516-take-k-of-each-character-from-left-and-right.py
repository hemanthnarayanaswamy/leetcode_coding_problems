class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        freq = Counter(s)

        # If we can't get k of each, impossible
        if freq['a'] < k or freq['b'] < k or freq['c'] < k:
            return -1
        
        # Sliding window over the middle segment we SKIP
        remaining = freq.copy()
        left = 0
        answer = n  # worst case: take everything

        for right in range(n):
            remaining[s[right]] -= 1

            # Shrink window while invalid
            while remaining['a'] < k or remaining['b'] < k or remaining['c'] < k:
                remaining[s[left]] += 1
                left += 1

            # Valid window → compute characters taken from ends
            take_count = left + (n - 1 - right)
            answer = min(answer, take_count)

        return answer
