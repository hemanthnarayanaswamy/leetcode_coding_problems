class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        total_chemistry = 0
        target_team_skill = skill[0] + skill[-1]

        for i in range(n // 2):
            left, right = skill[i], skill[n - 1 - i]

            if left + right != target_team_skill:
                return -1
            
            total_chemistry += (left * right)
        
        return total_chemistry