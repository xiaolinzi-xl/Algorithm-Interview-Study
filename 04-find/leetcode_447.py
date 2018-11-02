class Solution:
    @staticmethod
    def numberOfBoomerangs(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            distance = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dis = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + \
                    (points[i][1] - points[j][1]) * \
                    (points[i][1] - points[j][1])
                if dis in distance:
                    distance[dis] += 1
                else:
                    distance[dis] = 1

            for k, v in distance.items():
                res += v * (v-1)
    
        return res


def main():
    points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    print(Solution.numberOfBoomerangs(points))


if __name__ == '__main__':
    main()
