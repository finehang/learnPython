class Solution():
    '''换酒问题'''
    def numWaterBottles(self, numBottles: int, numExchange: int):
        numDrink, numEmpty = 0, 0  # 初始化喝的瓶数以及空瓶数
        numDrink += numBottles  # 把酒喝完
        numEmpty = numBottles  # 空瓶数
        i = 1
        while i:
            exchange = numEmpty // numExchange  # 空瓶换来的新酒数
            left = numEmpty % numExchange  # 不够交换的的空瓶数
            numEmpty -= exchange * numExchange  # 剩余的空瓶数
            numDrink += exchange  # 把换来的酒喝掉
            numEmpty = exchange + left  # 换来的酒喝掉后剩余的空瓶数
            if numEmpty < numExchange:  # 剩的还够不够换?
                return (numDrink)  # 不够就结束,并返回一共喝的酒瓶数
                i = 0


if __name__ == "__main__":
    S = Solution()
    print(S.numWaterBottles(20, 2))