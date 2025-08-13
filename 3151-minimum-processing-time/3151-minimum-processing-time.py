class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        time = 0
        
        for i, p in enumerate(processorTime):
            time = max(time, p + tasks[4*i])
        return time