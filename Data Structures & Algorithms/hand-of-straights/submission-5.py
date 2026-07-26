class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        c = Counter(hand)

        for num in hand:
            start = num
            # Find the left most element as the start
            while c[start - 1] > 0:
                start -= 1

            while start <= num:
                while c[start] > 0:
                    for i in range(start, start + groupSize):
                        if c[i] == 0:
                            return False
                        c[i] -= 1
                start += 1
        return True