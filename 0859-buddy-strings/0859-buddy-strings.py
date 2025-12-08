class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # need at least one duplicate to allow a no-op swap
            return any(c >= 2 for c in Counter(s).values())

        # collect mismatched positions
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]
        if len(diffs) != 2:
            return False
        (a1, b1), (a2, b2) = diffs
        return a1 == b2 and a2 == b1