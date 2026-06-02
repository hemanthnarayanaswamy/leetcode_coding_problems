class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_water = float('inf')
        water_land = float('inf')

        for ls,le in zip(landStartTime, landDuration):
            t1 = ls + le
            for ws, we in zip(waterStartTime, waterDuration):
                if t1 >= ws:
                    t2 = t1 + we
                else:
                    t2 = (ws - t1) + t1 + we
                land_water = min(land_water, t2)
        
        for ws, we in zip(waterStartTime, waterDuration):
            t1 = ws + we
            for ls,le in zip(landStartTime, landDuration):
                if t1 >= ls:
                    t2 = t1 + le
                else:
                    t2 = (ls - t1) + t1 + le
                water_land = min(water_land, t2)
        
        return min(water_land, land_water)
