class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Use binary search to find the left portion in the shorter array
        # such that I will get the remaining of the left portion from the 
        # other array correctly
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        # Guarnette medium, don't care l < r
        while True:

            # Edge of left portion in A
            mid =(l+r)//2
            
            lower_B = half - mid - 2
            
            # inf and -inf to cover the case that all lower portion come from
            # one of the array only
            Alower = A[mid] if mid >= 0 else float("-inf")
            Ahigher = A[mid + 1] if mid + 1 < len(A) else float("inf")
            Blower = B[lower_B] if lower_B >= 0 else float("-inf")
            Bhigher = B[lower_B + 1] if lower_B + 1 < len(B) else float("inf")

            if Blower <= Ahigher and Alower <= Bhigher:
                # Odd case
                if total % 2:
                    return min(Ahigher, Bhigher)
                return (max(Alower, Blower) + min(Ahigher, Bhigher)) / 2
            elif Alower > Bhigher:
                r = mid - 1
            else:
                l = mid + 1
