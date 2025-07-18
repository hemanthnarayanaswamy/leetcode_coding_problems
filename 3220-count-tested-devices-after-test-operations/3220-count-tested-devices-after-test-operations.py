class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        testedDevice = 0
        decreasedBattery = 0

        for b in batteryPercentages:
            if decreasedBattery:
                b = b - decreasedBattery 
            
            if b > 0:
                testedDevice += 1
                decreasedBattery += 1
        
        return testedDevice