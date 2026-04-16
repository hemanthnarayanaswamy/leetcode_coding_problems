class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        numsFreq = defaultdict(list)
        n = len(nums)

        for i, num in enumerate(nums):
            numsFreq[num].append(i)
        
        for q in queries:
            idx = q
            num = nums[idx]
            positions = numsFreq[num]

            if len(positions) < 2:
                answer.append(-1)
                continue

            # Find insertion point
            pos = bisect_left(positions, idx)

            # Find the exact index of idx inside positions
            if pos < len(positions) and positions[pos] == idx:
                k = pos

            m = len(positions)

            # neighbors (circular)
            prev_idx = positions[(k - 1) % m]
            next_idx = positions[(k + 1) % m]

            # circular distances
            d1 = min(abs(idx - prev_idx), n - abs(idx - prev_idx))
            d2 = min(abs(idx - next_idx), n - abs(idx - next_idx))

            answer.append(min(d1, d2))

        return answer