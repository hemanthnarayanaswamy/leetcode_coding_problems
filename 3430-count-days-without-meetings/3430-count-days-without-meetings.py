class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = 0
        meetings.sort()
        nextMeeting = 0
        for meeting in meetings:
            if nextMeeting < meeting[0]:
                count += (meeting[0] - nextMeeting) - 1
                nextMeeting = meeting[1]
            elif nextMeeting >= meeting[0]:
                if nextMeeting >= meeting[1]:
                    continue
                else:
                    nextMeeting = meeting[1]

        if nextMeeting < days:
            count += (days - nextMeeting)

        return count
        

        