import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        # build heap of (value, index)
        heap = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            val, idx = heapq.heappop(heap)     # O(log n)
            val *= multiplier
            nums[idx] = val                    # update the array in place
            heapq.heappush(heap, (val, idx))   # O(log n)

        return nums
