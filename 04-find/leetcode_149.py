# Definition for a point.
from decimal import Decimal


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n < 3:
            return n

        res = 2
        for i in range(n):
            record = {}
            flag = 1
            tmp = 0
            for j in range(i+1, n):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    flag += 1
                    continue
                if points[j].x - points[i].x != 0:
                    k = Decimal(points[j].y - points[i].y) / \
                        Decimal(points[j].x - points[i].x)
                else:
                    k = 1 << 100
                if k in record:
                    record[k] += 1
                else:
                    record[k] = 1
            # print(record)
            for v in record.values():
                tmp = max(tmp, v)
            res = max(res, tmp+flag)
        return res


if __name__ == "__main__":
    arr = [Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)]
    print(Solution().maxPoints(arr))
