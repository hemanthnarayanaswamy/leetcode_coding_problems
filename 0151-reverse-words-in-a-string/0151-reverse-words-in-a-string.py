import re

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.sub(' +', ' ', s).strip().split(' ')[:: -1])
        