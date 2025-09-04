class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        target = 0
        result = 0
        
        l, r = 0, len(skill)-1

        while l < r:
            a, b = skill[l], skill[r]
            if target and a+b != target:
                    return -1
            else:
                target = a + b
            result += (a*b)
            l += 1
            r -= 1
        
        return result

