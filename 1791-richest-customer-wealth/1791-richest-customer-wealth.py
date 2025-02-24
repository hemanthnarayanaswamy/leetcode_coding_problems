class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = []
        for account in accounts:
            max_wealth.append(sum(account))
        return max(max_wealth)