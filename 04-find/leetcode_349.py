class Solution:
    @staticmethod
    def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        res = set()
        for ele in nums2:
            if ele in nums1_set:
                res.add(ele)
        return list(res)

    @staticmethod
    def intersection_2(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        res = []
        for ele in nums2:
            if ele in nums1_set:
                res.append(ele)
                nums1_set.remove(ele)
        return res


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution.intersection(nums1, nums2))
    print(Solution.intersection_2(nums1, nums2))


if __name__ == '__main__':
    main()
