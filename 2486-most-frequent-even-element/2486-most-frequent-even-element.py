class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        result, mostFreq = -1, -1
        
        for num, freq in Counter(nums).items():
            if num % 2 == 0:
                if freq == mostFreq:
                    result = min(result, num)
                elif freq > mostFreq:
                    mostFreq = freq
                    result = num
        
        return result

