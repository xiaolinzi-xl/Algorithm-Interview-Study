class Solution:
    @staticmethod
    def minSubArrayLen(s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n + 1
        # [l,r] < s 为滑动窗口
        l, r = 0, -1
        sum_nums = 0
        while l < n:
            if sum_nums < s:
                if r+1 < n:
                    r += 1
                    sum_nums += nums[r]
                else:
                    break
            else:
                res = min(r-l+1, res)
                sum_nums -= nums[l]
                l += 1

        return res if res < n+1 else 0

    @staticmethod
    def minSubArrayLen_2(s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n + 1
        # [l,r] < s 为滑动窗口
        l, r = 0, -1
        sum_nums = 0
        while l < n:
            if r+1 < n and sum_nums < s:
                r += 1
                sum_nums += nums[r]
            else:
                sum_nums -= nums[l]
                l += 1
            if sum_nums >= s:
                res = min(r-l+1, res)

        return res if res < n+1 else 0


def main():
    s = 15
    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    print(Solution.minSubArrayLen(s, nums))
    print(Solution.minSubArrayLen_2(s, nums))


if __name__ == '__main__':
    main()
