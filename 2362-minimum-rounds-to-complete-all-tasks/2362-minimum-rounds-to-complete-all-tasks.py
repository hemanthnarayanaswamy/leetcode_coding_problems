class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasksFreq = Counter(tasks)
        count = 0

        for v in tasksFreq.values():
            if v == 1:
                return -1 
            
            q = v // 3
            r = v % 3

            if r == 0:
                count += q
            else:
                count += q + 1
        
        return count