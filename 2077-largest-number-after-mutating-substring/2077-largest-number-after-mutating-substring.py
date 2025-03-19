class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num_list = list(num)  
        mutation_started = False  # Flag to track mutation start

        for i in range(len(num_list)):
            digit = int(num_list[i])

            if change[digit] > digit:  # Start mutation if change[digit] > digit
                num_list[i] = str(change[digit])
                mutation_started = True
            elif change[digit] < digit and mutation_started:  
                # Stop as soon as we see a decreasing transformation
                break
            # If change[digit] == digit, we can continue mutation

        return ''.join(num_list)  # Convert list back to string
