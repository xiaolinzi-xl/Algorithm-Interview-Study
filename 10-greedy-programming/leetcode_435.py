# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        n = len(intervals)
        if n == 0:
            return 0

        intervals.sort(key=lambda x: x.end)
        res = 1
        index = 0
        for i in range(1, n):
            if intervals[i].start >= intervals[index].end:
                res += 1
                index = i

        return n - res
