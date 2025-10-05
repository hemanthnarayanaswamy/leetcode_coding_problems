class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        order_index = {val: idx for idx, val in enumerate(order)}
    
        # Sort friends based on their index in order; missing friends go to the end
        return sorted(friends, key=lambda x: order_index.get(x, len(order)))