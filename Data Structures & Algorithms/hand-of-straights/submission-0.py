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
        for _ in range(num_group):
            key = min(c.keys())
            g = []
            for i in range(groupSize):
                if c[key + i] > 0:
                    c[key + i] -= 1

                    if c[key + i] == 0:
                        c.pop(key + i)
                else:
                    return False

        return True