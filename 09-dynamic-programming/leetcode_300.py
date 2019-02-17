class Solution:

    def rebot(self, nums, index):
        if index == 0:
            return 1

        res = 1
        for i in range(index-1, -1, -1):
            if nums[index] > nums[i]:
                res = max(res, self.rebot(nums, i) + 1)

        return res

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        res = 0
        record = []
        for i in range(n):
            record.append(self.rebot(nums, i))
            res = max(res, self.rebot(nums, i))

        # print(record)
        return res

    def lengthOfLIS_1(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        res = 1
        memo = [1] * n

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)
            res = max(res, memo[i])

        # print(memo)
        return res


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [4, 10, 4, 3, 8, 9]
    print(Solution().lengthOfLIS(nums))
    print(Solution().lengthOfLIS_1(nums))
