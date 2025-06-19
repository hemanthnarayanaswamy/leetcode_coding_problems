class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        group=defaultdict(list)
        c=0
        for i,num in enumerate(nums):
            if num in group:
                for j in group[num]:
                    if (j*i)%k==0:
                        c+=1
            group[num].append(i)
        return c

        