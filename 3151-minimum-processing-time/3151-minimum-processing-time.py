class Solution:
    def minProcessingTime(self, processorTimes, taskTimes):
        processorTimes.sort()
        taskTimes.sort(reverse=True)
        answer = 0

        for i in range(len(processorTimes)):
            answer = max(answer, processorTimes[i] + taskTimes[i*4])
        
        return answer