class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            temp_wealth = sum(account)
            if temp_wealth > max_wealth:
                max_wealth = temp_wealth
        return max_wealth

        