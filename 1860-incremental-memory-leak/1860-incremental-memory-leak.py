class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        memory_req = 1

        while memory_req <= max(memory1, memory2):
            if memory1 >= memory2:
                memory1 -= memory_req
            else:
                memory2 -= memory_req
            
            memory_req += 1
        
        return [memory_req, memory1, memory2]