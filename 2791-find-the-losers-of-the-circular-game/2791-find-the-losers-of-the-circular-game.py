class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n
        i = 0
        step = 1
        while not visited[i]:
            visited[i] = True
            i = (i + step * k) % n
            step += 1
        return [idx + 1 for idx, seen in enumerate(visited) if not seen]
