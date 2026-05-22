class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.strip().split()
        
        for i in range(len(caption)):
            if i == 0:
                caption[i] = caption[i].lower()
            else:
                caption[i] = caption[i].capitalize()
        
        res = '#' + ''.join(caption)

        return res[:100]