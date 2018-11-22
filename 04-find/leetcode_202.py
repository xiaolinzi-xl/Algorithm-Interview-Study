class Solution:
    def digit_sum(self, n):
        res = 0
        while n > 0:
            tmp = n % 10
            n = n // 10
            res += tmp * tmp
        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = set()
        record.add(n)
        while True:
            res = self.digit_sum(n)
            if res == 1:
                return True
            if res in record:
                break
            record.add(res)
            n = res
        return False
