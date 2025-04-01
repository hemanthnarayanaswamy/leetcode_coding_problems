class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel_prefix = [0]

        for time in travel:
            travel_prefix.append(travel_prefix[-1]+time)
        
        overall_garbage = ''.join(garbage)
        t_m = overall_garbage.count('M')
        t_p = overall_garbage.count('P')
        t_g = overall_garbage.count('G')

        for i in range(len(garbage)-1, -1, -1):
            if 'M' in garbage[i]:
                t_m += travel_prefix[i]
                break

        for i in range(len(garbage)-1, -1, -1):
            if 'P' in garbage[i]:
                t_p += travel_prefix[i]
                break

        for i in range(len(garbage)-1, -1, -1):
            if 'G' in garbage[i]:
                t_g += travel_prefix[i]
                break

        return t_m + t_p + t_g
        