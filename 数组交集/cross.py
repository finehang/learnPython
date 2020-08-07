class Solution():
    def cross(self, a:list, b:list):
        c=[]
        for i in range(0,len(a)) :
            for j in range(0,len(b)):
                if a[i] == b[j]:
                    if b[j] not in c:
                        c.append(b[j])
        return c

if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,7]
    nums2 =[4,5,6,7,7,7,7,8,9]
    cross=Solution()
    print(cross.cross(nums1, nums2))