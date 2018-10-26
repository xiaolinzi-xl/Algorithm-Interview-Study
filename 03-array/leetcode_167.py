class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx1, idx2 = 0, len(numbers)-1
        while idx1 < idx2:
            if numbers[idx1] + numbers[idx2] == target:
                return [idx1+1, idx2+1]
            elif numbers[idx1] + numbers[idx2] > target:
                idx2 -= 1
            else:
                idx1 += 1
        return [-1, -1]


'''
时间复杂度：O(n)
空间复杂度：O(1)
'''


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    test = Solution()
    res = test.twoSum(numbers, target)
    print(res)


if __name__ == '__main__':
    main()
