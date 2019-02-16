class Solution:

    def rebot(self, nums, c, index):
        if c == 0:
            return True

        if index == len(nums) - 1:
            return nums[index] == c

        res = self.rebot(nums, c, index+1)

        if c >= nums[index]:
            res = res or self.rebot(nums, c-nums[index], index+1)

        return res

    def canPartition_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = 0
        for ele in nums:
            nums_sum += ele

        if nums_sum & 1 == 1:
            return False

        c = int(nums_sum / 2)
        return self.rebot(nums, c, 0)

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = 0
        for ele in nums:
            nums_sum += ele

        if nums_sum & 1 == 1:
            return False

        n = len(nums)
        c = int(nums_sum / 2)

        memo = [False] * (c+1)

        if c >= nums[-1]:
            memo[nums[-1]] = True

        for i in range(n-2, -1, -1):
            for j in range(c, nums[i]-1, -1):
                memo[j] = memo[j] or memo[j-nums[i]]

        return memo[c]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    # nums = [1, 2, 3, 5]
    print(Solution().canPartition(nums))
    print(Solution().canPartition_1(nums))
