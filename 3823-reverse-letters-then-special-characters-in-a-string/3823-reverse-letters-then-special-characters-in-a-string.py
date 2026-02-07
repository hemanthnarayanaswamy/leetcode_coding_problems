class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s)
        special_characters = '"!@#$%^&*()-+?_=,<>/"'
        def reverseLetter(s):
            l, r = 0, len(s)-1
            while l < r:
                if not s[l].isalpha():
                    l += 1
                elif not s[r].isalpha():
                    r -= 1
                else:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
            return s
        
        def reverseSpecialChar(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] not in special_characters:
                    print(s[l])
                    l += 1
                elif s[r] not in special_characters:
                    print(s[r])
                    r -= 1
                else:
                    print(s[l], s[r])
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
            return s
        
        s = list(s)
        s = reverseLetter(s)
        s = reverseSpecialChar(s)

        return ''.join(s)
        