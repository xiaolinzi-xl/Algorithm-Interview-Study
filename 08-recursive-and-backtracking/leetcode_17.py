class Solution:
    res = []
    digits_map = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def findCombinations(self, digits, index, s):
        if index == len(digits):
            Solution.res.append(s)
            return
        letter = digits[index]
        letter_str = Solution.digits_map[int(letter) - 2]

        for ele in letter_str:
            self.findCombinations(digits, index + 1, s + ele)

        return

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []

        Solution.res.clear()

        self.findCombinations(digits, 0, '')

        return Solution.res
