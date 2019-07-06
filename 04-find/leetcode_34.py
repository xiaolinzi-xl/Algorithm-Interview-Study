class Solution:
    def searchRange(self, nums, target):
        ans = [-1, -1]
        l, r = 0, len(nums) - 1
        # 查找右边界
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                ans[1] = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = 0, len(nums) - 1
        # 查找左边界
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                ans[0] = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return ans


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    print(Solution().searchRange(nums, 8))
