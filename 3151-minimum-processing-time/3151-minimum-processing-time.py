class Solution:
    def minProcessingTime(self, processorTimes, taskTimes):
        processorTimes.sort()
        taskTimes.sort(reverse=True)
        processorIndex = 0
        answer = 0

        for i in range(len(processorTimes)):
            currentMax = 0
            taskCount = 0

            answer = max(answer, processorTimes[i] + taskTimes[i*4])
        
        return answer