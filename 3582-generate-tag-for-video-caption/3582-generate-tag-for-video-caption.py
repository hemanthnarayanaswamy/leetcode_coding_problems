class Solution:
    def generateTag(self, caption: str) -> str:
        tag = ['#']
        caption = caption.strip().split()

        if not caption:
            return ''.join(tag)
        
        for i in range(len(caption)):
            if i == 0:
                tag.append(caption[i].lower())
            else:
                tag.append(caption[i].capitalize())
        
        return ''.join(tag)[:100]