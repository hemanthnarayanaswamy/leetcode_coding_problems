class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0]*n

        # Left to Right Prefix Operation 
        count = 0  # To track number of balls to the left
        operations = 0 # Operations required to move ball to current 

        for i in range(n):
            result[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count # Add Count to operations for the next position 

        # Right to Left Prefix Operation 
        count = 0  # To track number of balls to the right
        operations = 0 # Operations required to move ball to current 

        for i in range(n-1, -1, -1):
            result[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count # Add Count to operations for the next position 
        
        return result 