class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        startTime = 0
        maxTaskTime = 0
        EmpId = float('inf')

        for id, endTime in logs:
            taskTime = endTime - startTime
            if taskTime > maxTaskTime:
                EmpId = id
                maxTaskTime = taskTime
                print(EmpId, taskTime, maxTaskTime)
            elif taskTime == maxTaskTime:
                EmpId = min(id, EmpId)
            
            startTime = endTime
            
        return EmpId


