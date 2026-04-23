class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        numsIdx = defaultdict(list)

        for i, num in enumerate(nums):
            numsIdx[num].append(i)
        
        arr = [0] * len(nums)

        for idxs in numsIdx.values():
            total = sum(idxs)
            left_sum = 0
            m = len(idxs)

            for i in range(m):
                pos = idxs[i]
                right_sum = total - left_sum - pos

                left = pos * i - left_sum
                right = right_sum - pos * (m - i - 1)

                arr[pos] = left + right
                left_sum += pos
        
        return arr
