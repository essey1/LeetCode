class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r1 = len(nums1) -1
        r2 = n-1
        l1 = m-1
        while r1 >= 0:
            if r2>=0 and (l1<0 or nums2[r2] > nums1[l1]):
                nums1[r1] = nums2[r2]
                r2 -= 1
            elif l1>=0:
                nums1[r1] = nums1[l1]
                print(nums1)
                l1 -= 1
            r1 -= 1
        