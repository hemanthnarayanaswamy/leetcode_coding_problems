class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = 0
        meetings = sorted(meetings)
        nextMeeting = 0
        for meeting in meetings:
            startMeet, endMeet = meeting[0], meeting[1]
            if nextMeeting < startMeet:
                count += (startMeet - nextMeeting) - 1
            elif nextMeeting >= startMeet and nextMeeting >= endMeet:
                    continue
            
            nextMeeting = endMeet

        if nextMeeting < days:
            count += (days - nextMeeting)

        return count
        

        