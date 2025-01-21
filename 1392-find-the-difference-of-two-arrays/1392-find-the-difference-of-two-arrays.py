class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)

        ans1, ans2 = set(), set()

        for x in nums1:
            if x not in set2:
                ans1.add(x)
        
        for y in nums2:
            if y not in set1:
                ans2.add(y)
            
        return [list(ans1), list(ans2)]
