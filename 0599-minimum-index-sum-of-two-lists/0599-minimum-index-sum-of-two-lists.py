class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) == 1 and len(list2) == 1:
            return list1 # = list2
        
        hash_map = {word: i for i, word in enumerate(list1)}
        
        min_sum = 1000*2
        result = []
        for j, word in enumerate(list2):
            if word in hash_map:
                if hash_map[word] + j < min_sum:
                    min_sum = hash_map[word] + j
                    result = [word]
                elif hash_map[word] + j == min_sum:
                    result.append(word)

        return result
            