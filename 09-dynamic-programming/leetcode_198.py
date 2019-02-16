class Solution:

    def rebot(self, nums, index):
        if index == len(nums) - 1:
            return nums[index]

        if index >= len(nums):
            return 0

        return max(self.rebot(nums, index+2)+nums[index], self.rebot(nums, index+1))

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rebot(nums, 0)

    def rob_1(self, nums):
        if len(nums) == 0:
            return 0

        n = len(nums)
        memo = [0] * (n+1)
        memo[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            memo[i] = max(memo[i+2]+nums[i], memo[i+1])

        return memo[0]


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
    print(Solution().rob_1(nums))
