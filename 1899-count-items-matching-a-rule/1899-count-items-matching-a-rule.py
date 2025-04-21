class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_map = {"type": 0, "color": 1, "name": 2}
        itemCounter = 0
        idx = rule_map[ruleKey]

        for item in items:
            if item[idx] == ruleValue:
                itemCounter += 1
        
        return itemCounter