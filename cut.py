class Cut():
    def cut(self, n):
        m = 1
        for i in range(1, n+1):
            m += i
        return m



if __name__ == "__main__":
    c = Cut()
    print(c.cut(0))