class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if k >= n:
            return '0'

        stack = []
        i = 0

        while i < n and k > 0:
            if stack:
                if int(stack[-1]) > int(num[i]):
                    stack.pop()
                    k -= 1
                else:
                    stack.append(num[i])
                    i += 1
            else:
                stack.append(num[i])
                i += 1

        res = stack + list(num[i:])
        
        while k:
            res.pop()
            k -= 1
        
        res = (''.join(res)).lstrip('0')
        
        return res if res else '0'
                




