class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        nums = []
        idx_m, idx_n = 0, 0
        for i in range(m + n):
            if idx_m >= m:
                nums.append(nums2[idx_n])
                idx_n += 1
            elif idx_n >= n:
                nums.append(nums1[idx_m])
                idx_m += 1
            elif nums1[idx_m] < nums2[idx_n]:
                nums.append(nums1[idx_m])
                idx_m += 1
            else:
                nums.append(nums2[idx_n])
                idx_n += 1

        if (m + n) % 2 == 0:
            mid = (m + n) // 2
            return (nums[mid] + nums[mid - 1]) / 2
        return nums[(m + n) // 2]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
