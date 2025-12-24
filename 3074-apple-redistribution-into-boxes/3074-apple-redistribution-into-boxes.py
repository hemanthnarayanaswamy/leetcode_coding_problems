class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        cnt_apple=sum(apple)
        capacity.sort(reverse=True)
        cnt=0

        for c in capacity:
            if cnt_apple <=0:
                break        
            cnt_apple-=c
            cnt+=1

        return cnt