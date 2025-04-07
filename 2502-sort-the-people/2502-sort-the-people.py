class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_height = dict()
        for name,height in zip(names, heights):
            names_height[height] = name
        
        return [name for _,name  in sorted(names_height.items(), key=lambda item: item[0], reverse=True)]
        
