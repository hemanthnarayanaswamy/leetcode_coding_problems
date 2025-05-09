class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }

        result = ''

        def hundredThousandHandle(num):
            x = num // 100000
            num = num % 100000 
            tempRes = d[x] + ' '+ d[100] + ' ' +d[1000]

            if num < 1000:
                return tempRes, num 
            else:
                return d[x] + ' ' + d[100], num
        
        def uniqueNum1(num):
            if num > 100:
                Hun = (num // 100) 
                tempRes = d[Hun] + ' ' + d[100]
                restNum = num % 100

                if restNum in d:
                    return tempRes + ' ' + d[restNum]
                
                res = uniqueNum2(restNum)
                return tempRes + ' ' + res
            else:
                res = uniqueNum2(num)
                return res
        
        def uniqueNum2(num):
            Tens = (num // 10)*10
            Unit = num % 10

            if Tens != 0:
                return d[Tens] + ' ' + d[Unit]
            
            return d[Unit]


        while num > 0:
            if num >= 1000000000:
                x = num // 1000000000
                num = num % 1000000000
                
                if x == 100:
                    result += d[1] + ' ' + d[x] + ' ' + d[1000000000] + ' '

                result += d[x] + ' ' + d[1000000000] + ' '

            elif num >= 1000000:
                x = num // 1000000
                num = num % 1000000

                if x % 100 == 0:
                    y = x // 100
                    print(y)
                    print(result)
                    result += d[y] + ' ' + d[100] + ' ' + d[1000000] + ' '
                elif x in d:
                    result += d[x] + ' ' + d[1000000] + ' '
                else:
                    temp = uniqueNum1(x)
                    result += temp + ' ' + d[1000000] + ' '

            elif num >= 100000:
                temp, num =  hundredThousandHandle(num)
                result += temp + ' '

            elif num >= 1000:
                x = num // 1000
                num = num % 1000
                if x in d:
                    result += d[x] + ' ' + d[1000] + ' '
                else:
                    tempres = uniqueNum2(x)
                    result += tempres + ' ' + d[1000] + ' '

            elif num >= 100:
                x = num // 100
                num = num % 100

                result += d[x] + ' ' + d[100] + ' '

            elif num >= 10:
                if num in d:
                    result += d[num]
                    num = 0
                else:
                    x = (num // 10)*10
                    num = num % 10
                    result += d[x] + ' '
            else:
                result += d[num]
                num = 0

        return result.strip() if result else d[num]
