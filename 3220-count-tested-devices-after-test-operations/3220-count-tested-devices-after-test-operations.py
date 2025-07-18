class Solution:
    def countTestedDevices(self, battery_percentages: List[int]) -> int:
        tested_count = 0
        for battery in battery_percentages:
            # after testing tested_count devices, each remaining device has
            # “lost” tested_count% battery, so we can test this one iff
            # battery – tested_count > 0 ⇔ battery > tested_count
            if battery > tested_count:
                tested_count += 1
        return tested_count