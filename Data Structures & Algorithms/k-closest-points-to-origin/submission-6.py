class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # QuickSelect

        distance = lambda x, y:  math.sqrt(x ** 2 + y **2)

        def partition(l, r):
            pivot_d = distance(points[r][0], points[r][1])
            
            # Use last element as pivot
            pivot_idx = l
            for i in range(l, r):
                x, y = points[i]
                if distance(x, y) < pivot_d:
                    points[pivot_idx], points[i] = points[i], points[pivot_idx]
                    pivot_idx += 1
            
            # Plave pivot in the right position:
            points[pivot_idx], points[r] = points[r], points[pivot_idx]

            return pivot_idx
        l, r = 0, len(points) - 1
        pivot_idx = len(points)
        
        while pivot_idx != k:
            pivot_idx = partition(l, r)
            if pivot_idx < k:
                l = pivot_idx + 1
            else:
                r = pivot_idx - 1
        
        return points[:k]