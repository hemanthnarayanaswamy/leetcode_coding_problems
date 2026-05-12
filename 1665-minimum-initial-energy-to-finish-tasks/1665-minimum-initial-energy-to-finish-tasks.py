class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        sorted_tasks = sorted(tasks, key=lambda x: x[1]-x[0], reverse=True)
        initial_energy = 0
        remaining_energy = 0
    
        for energy, required_energy in sorted_tasks:
            if remaining_energy < required_energy:
                initial_energy += required_energy - remaining_energy
                remaining_energy += (required_energy - remaining_energy)
            remaining_energy -= energy
        
        return initial_energy

