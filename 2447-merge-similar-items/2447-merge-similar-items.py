class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items_combined = items1 + items2 
        items_hash = {}

        for item in items_combined:
            items_hash[item[0]] = items_hash.get(item[0], 0) + item[1]
        
        items_hash_sort = sorted(items_hash.items(), key=lambda item: item[0])

        return items_hash_sort

    


