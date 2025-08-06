class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasksFreq = Counter(tasks)
        count = 0

        for _, v in tasksFreq.items():
            if v < 2:
                return -1 
            
            count += (v - 1)//3 + 1

        return count