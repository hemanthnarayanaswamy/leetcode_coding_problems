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
            elif taskTime == maxTaskTime and id < EmpId:
                EmpId = id
                
            startTime = endTime
            
        return EmpId


