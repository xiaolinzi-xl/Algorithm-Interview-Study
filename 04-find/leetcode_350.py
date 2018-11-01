class Solution:
    @staticmethod
    def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_map = {}
        res = []
        for ele in nums1:
            if ele in nums1_map:
                nums1_map[ele] += 1
            else:
                nums1_map[ele] = 1

        for ele in nums2:
            if ele in nums1_map and nums1_map[ele] >= 1:
                res.append(ele)
                nums1_map[ele] -= 1

        return res


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution.intersect(nums1, nums2))


if __name__ == '__main__':
    main()
