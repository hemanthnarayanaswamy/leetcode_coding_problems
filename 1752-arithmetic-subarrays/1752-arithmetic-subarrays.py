class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        answer = [True]*m
        i = 0

        while i < m:
            sub_nums = sorted(nums[l[i]:r[i]+1])

            temp_diff = sub_nums[1] - sub_nums[0]
            
            for x in range(1, len(sub_nums)-1):
                if sub_nums[x+1] - sub_nums[x] != temp_diff:
                    answer[i] = False
                    break
            i += 1

        return answer
        