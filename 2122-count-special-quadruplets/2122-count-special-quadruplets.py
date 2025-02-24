class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        count = 0
        tot2 = {}  # Using a regular dictionary instead of defaultdict

        for c in range(2, len(nums) - 1):
            b = c - 1

            # Store all (nums[a] + nums[b]) sums in dictionary
            for a in range(b):
                pair_sum = nums[a] + nums[b]
                if pair_sum in tot2:
                    tot2[pair_sum] += 1  # Increment count if already exists
                else:
                    tot2[pair_sum] = 1  # Initialize the sum count

            # Check for valid quadruplets (nums[d] - nums[c] == nums[a] + nums[b])
            for d in range(c + 1, len(nums)):
                target = nums[d] - nums[c]
                if target in tot2:
                    count += tot2[target]  # Add valid quadruplets found

        return count
