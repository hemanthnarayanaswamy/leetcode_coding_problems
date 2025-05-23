class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()

        for i in range(len(title)):
            word = title[i]
            if len(word) > 2:
                title[i] = word.capitalize()
            else:
                title[i] = word.lower()
        
        return " ".join(title)
