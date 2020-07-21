class Rome():
    def main(self, num):
        count_m = num // 1000
        num = num % 1000
        count_d = num // 500
        num = num % 500
        count_c = num // 100
        num = num % 100
        count_l = num // 50
        num = num % 50
        count_x = num // 10
        num = num % 10
        count_v = num // 5
        num = num % 5
        count_i = num // 1
        num = num % 1
        result = 'M'*count_m+'D'*count_d+'C'*count_c+'L'*count_l+'X'*count_x+'V'*count_v+'I'*count_i
        a = 1
        print('原式为',result)
        while a:
            if 'VIIII' in result:
                result = result.replace('VIIII', 'IX')
                continue
            elif 'IIII' in result:
                result = result.replace('IIII', 'IV')
                continue
            elif 'LXXXX' in result:
                result = result.replace('LXXXX', 'XC')
                continue
            elif 'XXXX' in result:
                result = result.replace('XXXX', 'XL')
                continue
            elif 'DCCCC' in result:
                result = result.replace('DCCCC', 'CM')
                continue
            elif 'CCCC' in result:
                result = result.replace('CCCC', 'CD')
                continue
            # if 'VIIII' or 'IIII' or 'LXXXX' or 'XXXX' or 'DCCCC' or 'CCCC' not in result:
            a = 0
        return result

if __name__ == "__main__":
    Rome = Rome()
    print('简化后为',Rome.main(99))