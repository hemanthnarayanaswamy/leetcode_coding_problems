class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        arrIdx = defaultdict(list)

        for i, num in enumerate(arr):
            arrIdx[num].append(i)

        intervals = [0] * len(arr)

        for idxs in arrIdx.values():
            prefix = [0]
            total_sum = sum(idxs)
            left_sum = 0
            m = len(idxs)

            for i, pos in enumerate(idxs):
                right_sum = total_sum - left_sum - pos

                left = pos*i - left_sum
                right = right_sum - (m - i - 1)*pos

                intervals[pos] = left + right

                left_sum += pos
        
        return intervals
