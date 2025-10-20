class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for opx in operations:
            if '+' in opx:
                x += 1
            else: 
                x -= 1
        
        return x