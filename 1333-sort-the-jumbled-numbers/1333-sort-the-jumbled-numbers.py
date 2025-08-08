class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapNums(num):
            res = []
            for i in str(num):
                tmp = str(mapping[int(i)])
                res.append(tmp)
            
            newNum = (''.join(res)).lstrip('0')

            return int(newNum) if newNum else 0
        
        return sorted(nums, key=mapNums)

        