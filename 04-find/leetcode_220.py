class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        l, r = 0, 0
        # [l,r) 为符合条件的元素
        record = set()

        while r < len(nums):
            res = self.ceil(record, nums[r]-t)
            if res != None and res <= nums[r] + t:
                return True

            record.add(nums[r])
            r += 1

            if len(record) == k + 1:
                record.remove(nums[l])
                l += 1

        return False

    def ceil(self, record, x):
        res = 0xfffffff
        for ele in record:
            if ele >= x:
                res = min(ele, res)

        return res if res != 0xfffffff else None


'''
时间超出限制
时间复杂度：O(nlogk)
空间复杂度为：O(k)
'''


def main():
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))


if __name__ == '__main__':
    main()
