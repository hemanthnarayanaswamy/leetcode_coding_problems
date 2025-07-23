class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # generic “remove all occurrences of XY in one pass, scoring score_per_pair”
        def remove_pairs(seq: List[str], X: str, Y: str, score_per_pair: int):
            stack = []
            total = 0
            for c in seq:
                if c == Y and stack and stack[-1] == X:
                    stack.pop()
                    total += score_per_pair
                else:
                    stack.append(c)
            # return both your score and the leftovers (to feed into the next remover)
            return total, stack

        # decide which pair to rip out first
        if x >= y:
            gain1, rem = remove_pairs(list(s), 'a', 'b', x)
            gain2, _   = remove_pairs(rem, 'b', 'a', y)
        else:
            gain1, rem = remove_pairs(list(s), 'b', 'a', y)
            gain2, _   = remove_pairs(rem, 'a', 'b', x)

        return gain1 + gain2
