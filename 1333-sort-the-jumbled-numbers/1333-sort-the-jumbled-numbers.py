class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num):
            mapped_str = ""
            for digit in str(num):
                mapped_str += str(mapping[int(digit)])
            return int(mapped_str)
        
        return sorted(nums, key=get_mapped_value)
            