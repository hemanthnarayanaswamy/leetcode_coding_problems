class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            while len(stack) >= 2:
                prev = stack[-2]
                curr = stack[-1]

                if prev[0] == '(' and prev[1] >= k and curr[1] >= k:
                    stack.pop()

                    if prev[1] == k:
                        stack.pop()
                    else:
                        prev[1] -= k
                else:
                    break
        
        return ''.join(ch * cnt for ch, cnt in stack)
        

            