class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map_lst1 = {}
        comm_str = []
        min_idxSum = float('inf')

        for i,s in enumerate(list1):
            map_lst1[s] = i
        
        for i,s in enumerate(list2):
            if s in map_lst1:
                tmp_sum = i + map_lst1[s]
                
                if tmp_sum < min_idxSum:
                    comm_str.clear()
                    comm_str.append(s)
                    min_idxSum = tmp_sum
                elif tmp_sum == min_idxSum:
                    comm_str.append(s)
        
        return comm_str
            
        
