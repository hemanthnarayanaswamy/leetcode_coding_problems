class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = {}
        n = len(nums)

        for i in range(n - 1):
            x = nums[i]
            if x == key:
                y = nums[i+1]
                count[y] = count.get(y, 0) + 1
        
        num, freq = 0, 0

        for k, v in count.items():
            if v > freq:
                num = k
                freq = v

        return num

            

