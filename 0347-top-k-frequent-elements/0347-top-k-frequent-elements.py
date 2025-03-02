class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums)
        ## Sorting the Dictionary by the values 
        ## {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        nums_freq = {k: v for k, v in sorted(nums_freq.items(), reverse = True, key=lambda item: item[1])}
        result = []
        for keys in nums_freq:
            result.append(keys)
            k -= 1
            if k == 0:
                return result 
        return result