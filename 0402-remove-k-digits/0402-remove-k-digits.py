class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        
        if k >= n:
            return '0'
        
        stack = []
        i = 0
        
        # Phase 1: Greedy removal using stack
        while i < n and k > 0:
            # Remove digits from stack if current digit is smaller
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        
        # Add remaining digits
        while i < n:
            stack.append(num[i])
            i += 1
        
        # Phase 2: Remove remaining k digits from end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Phase 3: Handle leading zeros and empty result
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'

