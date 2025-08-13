class Solution:
    def minProcessingTime(self, processorTimes, taskTimes):
        processorTimes.sort()
        taskTimes.sort(reverse=True)
        answer = 0

        for i in range(len(processorTimes)):
            val = processorTimes[i] + taskTimes[i*4]
            if val > answer:
                answer = val
        
        return answer