class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        n = len(A) + len(B)
        n_half = n // 2
        
        if len(B) < len(A):
            A, B = B, A
        
        len_A, len_B = len(A), len(B)
        
        l, r = 0, len_A - 1

        while True:
            i = (l + r) // 2  # For A
            j = n_half - i - 2  # For B

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i + 1] if (i + 1) < len_A else float('inf')
            
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j + 1] if (j + 1) < len_B else float('inf')

            # Check if partition is correct
            if A_left <= B_right and B_left <= A_right:
                # Check for odd
                if n % 2:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                r = i - 1
            
            else:
                l = i + 1
