class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        skillVal = set()
        result = 0
        
        l, r = 0, len(skill)-1

        while l < r:
            a, b = skill[l], skill[r]
            if skillVal and a+b not in skillVal:
                    return -1
            else:
                skillVal.add(skill[l] + skill[r])
            result += (a*b)
            l += 1
            r -= 1
        
        return result

