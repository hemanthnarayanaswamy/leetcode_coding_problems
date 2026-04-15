class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = remaining = Counter(s)
        n = len(s)
        
        if not k:
            return k

        if freq['a'] < k or freq['b'] < k or freq['c'] < k:
            return -1
        
        left = 0
        answer = n
        for right in range(n):
            c = s[right]
            remaining[c] -= 1

            while remaining[c] < k:
                remaining[s[left]] += 1
                left += 1
            
            take_count = left + (n - 1 - right)
            answer = min(answer, take_count)
        
        return answer
