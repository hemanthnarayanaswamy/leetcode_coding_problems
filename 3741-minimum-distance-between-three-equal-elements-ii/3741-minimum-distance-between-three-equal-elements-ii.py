class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def absDist(arr):
            minDist = float('inf')
            for idx in range(2, len(arr)):
                i, j, k = arr[idx-2], arr[idx-1], arr[idx]
                dist = abs(i - j) + abs(j - k) + abs(k - i)
                if dist < minDist:
                    minDist = dist
            return minDist

        freq = Counter(nums)
        elements = set()
        elementIdx = defaultdict(list)

        for num in freq:
            if freq[num] >= 3:
                elements.add(num)
        
        if not elements:
            return -1
        
        for i, num in enumerate(nums):
            if num in elements:
                elementIdx[num].append(i)
        
        minDist = float('inf')
        
        for arr in elementIdx.values():
            dist = absDist(arr)
            if dist < minDist:
                minDist = dist
        
        return minDist
