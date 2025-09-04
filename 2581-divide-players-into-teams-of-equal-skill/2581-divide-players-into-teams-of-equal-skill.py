class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        target = skill[0] + skill[-1]
        result = skill[0] * skill[-1]

        if n == 2:
            return result
        
        l, r = 1, n-2

        while l < r:
            a, b = skill[l], skill[r]
            if a+b != target:
                return -1
            result += (a*b)
            l += 1
            r -= 1
        
        return result

