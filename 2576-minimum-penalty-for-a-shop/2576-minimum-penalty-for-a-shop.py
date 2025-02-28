class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        min_penalty = float('inf')  # Store the minimum penalty found
        best_time = 0  # Store the best closing time
        penalty = customers.count('Y')  # Initial penalty if the shop closes at j = 0

        if "Y" not in customers:
            return 0
        if "N" not in customers:
            return n

        for j in range(n + 1):  # Check all possible closing times (0 to n)
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = j  # Store the earliest minimum penalty closing hour
            
            if j < n:
                # If shop is open at 'N' (no customers), increase penalty
                # If shop is closed at 'Y' (customers inside), decrease penalty
                penalty += -1 if customers[j] == 'Y' else 1  
            
        return best_time
