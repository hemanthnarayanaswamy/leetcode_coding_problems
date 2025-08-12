class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers:
            return 0.0
        
        total_waiting_time = 0
        chef_available_time = 0

        for arrival_time, cooking_time in customers:
            cooking_start_time = max(arrival_time, chef_available_time)

            food_ready_time = cooking_start_time + cooking_time 

            total_waiting_time += (food_ready_time - arrival_time)

            chef_available_time = food_ready_time
        
        return total_waiting_time / len(customers)