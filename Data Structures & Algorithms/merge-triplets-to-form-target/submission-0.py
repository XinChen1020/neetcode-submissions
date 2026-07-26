class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Due to max opertion, triplets with larger value than corresponding element
        # in target would not be usable. 
        a, b, c = False, False, False
        for t in triplets:

            if t[0] > target[0] or \
            t[1] > target[1] or \
            t[2] > target[2]:
                continue
            
            if t[0] == target[0]:
                a = True
            if t[1] == target[1]:
                b = True
            if t[2] == target[2]:
                c = True

        return a and b and c