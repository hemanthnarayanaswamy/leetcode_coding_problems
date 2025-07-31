class Solution:
    def maxPower(self, s: str) -> int:
        max_power = current_power = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_power += 1
            else:
                if current_power > max_power:
                    max_power = current_power
                current_power = 1
        
        return max(max_power, current_power)