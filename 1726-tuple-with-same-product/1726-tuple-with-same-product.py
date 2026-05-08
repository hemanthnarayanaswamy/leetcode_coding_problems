class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        productFreq = defaultdict(int)

        for i in range(n):
            for j in range(i+1, n):
                    productFreq[nums[i]*nums[j]] += 1
        
        print(productFreq)
        totalTuples = 0
        for v in productFreq.values(): # v = number of unique pairs with the same product
            totalTuples += (v * (v - 1) // 2) * 8
        
        return totalTuples