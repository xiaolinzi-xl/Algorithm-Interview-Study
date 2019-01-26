class Solution:
    res = []
    used_flag = []

    def generatePermutation(self, nums, index, p):
        if index == len(nums):
            Solution.res.append(list(p))
            return
       
        for i in range(len(nums)):
            if not Solution.used_flag[i]:
                Solution.used_flag[i] = True
                p.append(nums[i])
                self.generatePermutation(nums, index + 1, p)
                Solution.used_flag[i] = False
                p.pop()

        return

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        Solution.res.clear()
        Solution.used_flag = len(nums) * [False]

        self.generatePermutation(nums, 0, [])
        return Solution.res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
