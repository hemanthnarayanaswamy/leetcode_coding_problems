class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        offlineTime = {str(i): 0 for i in range(numberOfUsers)}
        mentioned = {str(i): 0 for i in range(numberOfUsers)}
        order = {'OFFLINE': 0, 'MESSAGE': 1}
        
        def processMessage(t, users):
            if users == 'ALL':
                for k in mentioned:
                    mentioned[k] += 1
            elif users == 'HERE':
                for k in mentioned:
                    if (offlineTime[k] and t >= offlineTime[k]) or not offlineTime[k]:
                        mentioned[k] += 1
            else:
                users = users.split()
                for user in users:
                    id = user[2:]
                    mentioned[id] += 1
        
        events = sorted(events, key=lambda x: (int(x[1]), order[x[0]]))
        for event in events:
            e, t, users = event[0], int(event[1]), event[2]

            if e == 'OFFLINE':
                offlineTime[users] = t + 60
            elif e == 'MESSAGE':
                processMessage(t, users)
                
        return [mentioned[k] for k in mentioned]