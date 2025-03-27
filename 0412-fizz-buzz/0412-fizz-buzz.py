class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for num in range(1, n+1):
            ans_3 = num % 3
            ans_5 = num % 5

            if ans_3 != 0 and ans_5 != 0:
                answer.append(str(num))
            elif ans_3 == 0 and ans_5 == 0:
                answer.append("FizzBuzz")
            elif ans_3 == 0:
                answer.append("Fizz")  
            else:
                answer.append("Buzz")
        return answer
        
        