class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(start1, duration1, start2, duration2):
            t1 = float('inf')
            for i in range(len(start1)):
                t1 = min(t1, start1[i] + duration1[i])

            t2 = float('inf')
            for i in range(len(start2)):
                t2 = min(t2, max(start2[i], t1) + duration2[i])

            return t2

        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_water, water_land)
        