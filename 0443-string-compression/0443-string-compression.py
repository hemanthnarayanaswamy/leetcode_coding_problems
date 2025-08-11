class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1

        count = 1
        newChars = []

        for i in range(1, n):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count > 1:
                    newChars.append(chars[i-1])
                    newChars.extend(list(str(count)))
                    count = 1
                else:
                    newChars.append(chars[i-1])
            
        newChars.append(chars[i])

        if count > 1:
            newChars.extend(list(str(count)))

        chars[:n] = newChars

        return len(chars)