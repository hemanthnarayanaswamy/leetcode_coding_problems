class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        lenN = len(nums)
        uniq_quad = 0
        for a in range(lenN-3):
            for b in range(a+1,lenN):
                for c in range(b+1,lenN):
                    for d in range(c+1,lenN):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                                uniq_quad +=1

        return uniq_quad
                            
