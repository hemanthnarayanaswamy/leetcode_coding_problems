class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count_freq = {}
        result = []

        for num in nums:
            if num not in count_freq:
                count_freq[num] = 0
            
            idx = count_freq[num]
            if idx >= len(result):
                result.append([])
            
            result[idx].append(num)
            count_freq[num] += 1
        return result