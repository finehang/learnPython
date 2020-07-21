class Rome():
    def main(self, str1):
        result = 0
        dt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(1, len(str1)):
            if dt[str1[i]] > dt [str1[i-1]]:
                result -= dt[str1[i-1]]
            else:
                result += dt[str1[i-1]]
        return result + dt[str1[-1]]


if __name__ == "__main__":
    Rome = Rome()
    print(Rome.main('MCMXCIV'))