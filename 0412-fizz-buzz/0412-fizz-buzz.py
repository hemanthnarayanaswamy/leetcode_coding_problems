class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [] # Return the Answer

        for num in range(1, n+1):
            ans_3 = num % 3  # Store the values to reassess 
            ans_5 = num % 5

            if ans_3 != 0 and ans_5 != 0:
                answer.append(str(num))

            elif ans_3 == 0:
                if ans_5 == 0:
                     answer.append("FizzBuzz")
                else:
                    answer.append("Fizz") 
            else:
                answer.append("Buzz")
                
        return answer
        
        