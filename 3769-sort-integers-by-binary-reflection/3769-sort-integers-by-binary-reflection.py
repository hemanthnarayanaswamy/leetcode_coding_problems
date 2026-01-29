class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        numsRev = []

        for num in nums:
            ref = int(bin(num)[-1:1:-1], 2)
            numsRev.append((ref, num))

        numsRev.sort()
        
        return [num for ref, num in numsRev]