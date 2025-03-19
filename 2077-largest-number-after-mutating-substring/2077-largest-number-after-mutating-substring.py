class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        change_map = {i:num for i, num in enumerate(change)}
        result = [] 
        i = 0
        mutate = False 
        while i < len(num):
            if int(num[i]) < change_map[int(num[i])]:
                result.append(str(change_map[int(num[i])]))
                i += 1
                mutate = True 
                while mutate and i < len(num):
                    if int(num[i]) > change_map[int(num[i])]:
                        result.append(num[i:len(num)])
                        i = len(num)
                        break
                    else:
                        result.append(str(change_map[int(num[i])]))
                        i += 1
            else:
                result.append(num[i])
                i += 1                

        return ''.join(result)



        