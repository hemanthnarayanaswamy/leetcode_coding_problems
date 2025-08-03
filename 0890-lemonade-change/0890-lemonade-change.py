class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        myCounter = {5: 0, 10: 0}

        for cash in bills:
            if cash == 20:
                if myCounter[10] != 0 and myCounter[5] != 0:
                    myCounter[10] = myCounter.get(10) - 1
                    myCounter[5] = myCounter.get(5) - 1
                elif myCounter[10] == 0 and myCounter[5] >= 3:
                    myCounter[5] = myCounter.get(5) - 3
                else:
                    return False
            elif cash == 10:
                if myCounter[5] == 0:
                    return False
                else:
                    myCounter[5] = myCounter.get(5) - 1
                    myCounter[10] = myCounter.get(10) + 1
            else:
                myCounter[5] = myCounter.get(5) + 1

        return True




            