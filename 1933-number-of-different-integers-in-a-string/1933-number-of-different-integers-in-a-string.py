class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        start_idx = 0
        in_digit_sequence = False
        numbers = set()

        for i, char in enumerate(word):
            if char.isdigit():
                if not in_digit_sequence:
                    start_idx = i
                    in_digit_sequence = True
                if i == len(word) - 1:
                    numbers.add(int(word[start_idx:i + 1]))
            else:
                if in_digit_sequence:
                    numbers.add(int(word[start_idx:i]))
                    in_digit_sequence = False

        return len(numbers)