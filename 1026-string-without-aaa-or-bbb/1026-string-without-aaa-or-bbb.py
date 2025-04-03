class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = ''
        total_lenght = a+b

        while len(result) < total_lenght:
            if a > b:
                result += 'aab'
                a -= 2
                b -= 1
            elif b > a:
                result += 'bba'
                b -= 2
                a -= 1
            else:
                result += 'ab'
                a -= 1
                b -= 1

            if a == 0 or b == 0:
                if a == 0:
                    result += 'b'*b
                    break
                else:
                    result += 'a'*a
                    break

        return result
        