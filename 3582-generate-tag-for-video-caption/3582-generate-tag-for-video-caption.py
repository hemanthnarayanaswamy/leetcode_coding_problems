class Solution:
    def generateTag(self, caption: str) -> str:
        tag = '#'
        caption = caption.strip().split()

        if not caption:
            return tag
        
        caption[0] = caption[0].lower()

        
        for i in range(1, len(caption)):
                caption[i] = caption[i].capitalize()
        
        tag += "".join(caption)
        return tag[:100]