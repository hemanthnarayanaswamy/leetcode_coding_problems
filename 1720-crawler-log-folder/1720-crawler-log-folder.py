class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0

        for dir in logs:
            if dir == '../':
                if count == 0:
                    continue
                else:
                    count -= 1
            elif dir == './':
                continue
            else:
                count += 1
        
        return count