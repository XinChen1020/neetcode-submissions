from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand must be multiple of groupSize
        if len(hand) % groupSize != 0:
            return False
        
        num_group = len(hand) // groupSize

        # How to form the group
        # Always start with the smallest and go up until groupSize
        # then repeat from the smallest again
        c = Counter(hand)
        
        # Start with all groups at the same time
        for k in sorted(c.keys()):
            if c[k] > 0:
                num_group = c[k]

                for i in range(groupSize):
                    if c[k + i] < num_group:
                       return False
                    c[k + i] -= num_group

        return True