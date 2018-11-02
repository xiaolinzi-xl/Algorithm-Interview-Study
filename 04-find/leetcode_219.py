class Solution:
    @staticmethod
    def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l, r = 0, 0
        # [l,r) 为 不重复元素
        nums_set = set()
        while r < len(nums):
            if nums[r] in nums_set:
                return True
            nums_set.add(nums[r])
            r += 1

            if r - l > k:
                nums_set.remove(nums[l])
                l += 1

        return False


def main():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(Solution.containsNearbyDuplicate(nums, k))


if __name__ == '__main__':
    main()
