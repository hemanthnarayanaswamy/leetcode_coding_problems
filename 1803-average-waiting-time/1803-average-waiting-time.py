class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_wait = 0
        
        for arrival, duration in customers:
            if current_time < arrival:
                current_time = arrival  
                
            current_time += duration
            total_wait += current_time - arrival  

        return total_wait / len(customers)