class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right_shift_sum = [0]*len(boxes)
        left_shift_sum = [0]*len(boxes)

        for i in range(len(boxes)):
            for j in range(i+1, len(boxes)):
                if boxes[j] == '1':
                    right_shift_sum[i] += (j - i)
        
        for i in range(len(boxes)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if boxes[j] == '1':
                    left_shift_sum[i] += (i - j)

        return [x+y for x,y in zip(right_shift_sum, left_shift_sum)]
        