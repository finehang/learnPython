class Solution():
    '''换酒问题'''
    def numWaterBottles(self, numBottles: int, numExchange: int):
        return (numBottles * numExchange - 1) // (numExchange - 1)


if __name__ == "__main__":
    S = Solution()
    print(S.numWaterBottles(20, 3))