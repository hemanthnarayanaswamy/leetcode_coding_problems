class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        orderFreq = {o:i for i,o in enumerate(order)}
        def position(friend):
            return orderFreq[friend]
        
        friends = sorted(friends, key=position)
        return friends