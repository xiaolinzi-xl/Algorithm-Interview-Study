class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ele in s:
            if ele in ('[', '(', '{'):
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return False
                tmp = stack.pop(-1)
                if tmp+ele not in ('[]', '()', '{}'):
                    return False

        if len(stack) != 0:
            return False
        return True
