class Solution:
    '''
    给定一个非负整数数组和一个整数 m，
    你需要将这个数组分成 m 个非空的连续子数组。
    设计一个算法使得这 m 个子数组各自和的最大值最小。
    '''
    def spliteArray(self, nums, m):
        left = max(nums)  # 二分法,最小值为数组中最大值
        right = sum(nums)  # 最大值不超过数组之和
        def check(mid):  # 检查函数,检查left 和right的中值是否符合条件
            total, cnt = 0, 1
            for i in nums:
                if total + i > mid:  # 子组之和不应超过中值
                    cnt += 1
                    total = i  # 超过,就划分下一子组
                else:
                    total += i  # 不超过就继续向后加
            return cnt <= m

        while left < right:  # 只要左值小于右值
            mid = (left + right)//2  # 取中值
            if check(mid):  # 检查中值是否符合条件
                right = mid  # 子组少于给定的,说明右值太大
            else:
                left = mid + 1  # 子组多于给定的,说明左值太小
        return left
            



if __name__ == "__main__":
    s = Solution()
    print(s.spliteArray([7,2,5,10,8], 2))