class Solution:

    # 暴力解法
    def maxArea(self, height):
        res = min(height[0], height[1])

        for i in range(1, len(height)):
            area = 0
            for j in range(i):
                tmp = min(height[i], height[j]) * (i - j)
                area = max(area, tmp)
            res = max(area, res)

        return res

    # 双指针
    def maxArea_1(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(area, ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
    print(Solution().maxArea_1(height))
