class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_ref = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        text_ballon = {}

        for letter in text:
            if letter in balloon_ref:
                text_ballon[letter] = text_ballon.get(letter, 0) + 1

        # Calculate the maximum number of "balloon" words that can be formed
        return min(text_ballon.get(letter, 0) // balloon_ref[letter] for letter in balloon_ref)