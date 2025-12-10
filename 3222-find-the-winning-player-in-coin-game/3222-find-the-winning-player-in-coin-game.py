class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        play = False

        while x and y:
            x -= 1
            y -= 4

            if x < 0 or y < 0:
                break
            else:
                play = not play
        
        return "Alice" if play else "Bob"
