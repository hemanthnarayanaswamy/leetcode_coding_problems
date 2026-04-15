class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        remaining = Counter(s)

        # If we can't get k of each, impossible
        if remaining['a'] < k or remaining['b'] < k or remaining['c'] < k:
            return -1
        
        left = 0
        answer = n  # worst case: take everything

        for right in range(n):
            remaining[s[right]] -= 1

            # Shrink window while invalid
            while remaining['a'] < k or remaining['b'] < k or remaining['c'] < k:
                remaining[s[left]] += 1
                left += 1

            # Valid window → compute characters taken from ends
            answer = min(answer, n - (right - left + 1))

        return answer
