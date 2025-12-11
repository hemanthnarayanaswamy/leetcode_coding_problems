class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        startTime = 0
        maxTaskTime = 0
        EmpId = None

        for id, endTime in logs:
            taskTime = endTime - startTime
            if taskTime > maxTaskTime:
                EmpId = id
                maxTaskTime = taskTime
            elif taskTime == maxTaskTime:
                EmpId = min(id, EmpId)
            
            startTime = endTime
            
        return EmpId


