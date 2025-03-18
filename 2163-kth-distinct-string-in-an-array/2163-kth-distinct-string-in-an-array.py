from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        char_map = Counter(arr)

        for char in char_map:
            if char_map[char] != 1:
                continue
            if k == 1:
                return char
            k -= 1
        return ''
            
            

        