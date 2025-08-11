class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        count = 1
        newChars = []

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count > 1:
                    newChars.append(chars[i-1])
                    newChars.extend(list(str(count)))
                    count = 1
                else:
                    newChars.append(chars[i-1])
            print(newChars)

        newChars.append(chars[i])
        if count > 1:
            newChars.extend(list(str(count)))

        chars[:len(chars)] = newChars

        return len(chars)