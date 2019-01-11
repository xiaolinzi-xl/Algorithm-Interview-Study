from queue import PriorityQueue as PQueue


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        record = {}
        for ele in nums:
            if ele in record:
                record[ele] += 1
            else:
                record[ele] = 1

        pq = PQueue()
        for key, v in record.items():
            if len(pq.queue) < k:
                pq.put((v, str(key)))
            else:
                tmp = pq.get()
                if tmp[0] < v:
                    pq.put((v, str(key)))
                else:
                    pq.put(tmp)

        res = []
        for ele in pq.queue:
            res.append(int(ele[1]))

        return res


if __name__ == "__main__":
    nums = [6, 0, 1, 4, 9, 7, -3, 1, -4, -8, 4, -7, -3, 3, 2, -3, 9, 5, -4, 0]
    k = 6
    print(Solution().topKFrequent(nums, k))
