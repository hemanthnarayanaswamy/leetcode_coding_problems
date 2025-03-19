class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)  
        mutation_started = False  # Flag to track mutation start

        for i in range(len(num)):
            digit = int(num[i])

            if change[digit] > digit:  # Start mutation if change[digit] > digit
                num[i] = str(change[digit])
                mutation_started = True
            elif change[digit] < digit and mutation_started:  
                # Stop as soon as we see a decreasing transformation
                break


        return ''.join(num)  # Convert list back to string
