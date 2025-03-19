class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        #change_map = {i:num for i, num in enumerate(change)}
        num = [s for s in num] 
        i = 0 
        while i < len(num):
            if int(num[i]) < change[int(num[i])]:
                while i < len(num):
                    if int(num[i]) > change[int(num[i])]:
                        return ''.join(num)
                    else:
                        num[i] = str(change[int(num[i])])
                        i += 1
            i += 1               

        return ''.join(num)



        