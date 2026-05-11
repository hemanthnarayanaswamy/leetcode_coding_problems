class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = defaultdict(set)
        for user_id, time in logs:
            user_minutes[user_id].add(time)

        count = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            count[uam - 1] += 1

        return count