class Solution:
    res = []

    def rebot(self, idx, nums):
        if idx >= len(nums):
            self.res.append([nums[idx] for idx in range(len(nums)) if self.visited[idx]])
            return

        self.visited[idx] = True
        self.rebot(idx + 1, nums)

        self.visited[idx] = False
        self.rebot(idx + 1, nums)

    def subsets(self, nums):
        self.res.clear()
        self.visited = [False] * len(nums)

        self.rebot(0, nums)
        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
