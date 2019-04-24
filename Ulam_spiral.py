"""
function generating Ulam spiral
"""
def ulam(n):
    if n % 2 == 1:
        liczby = [i for i in range(n**2, 0, -1)]
        r = int(n / 2 + 1)
        spirala = [[] for i in range(n)]
        check = n-1
        check2 = 0
        check3 = n
        while check+1 != 0:
            if not liczby:
                break
            for i in range(r):
                for j in range(check3):
                    spirala[check].insert(check2, liczby[0])
                    del liczby[0]
                if not liczby:
                    break
                for j in range(check-1, check2-1, -1):
                    spirala[j].insert(check2, liczby[0])
                    del liczby[0]
                if check2 == 0:
                    for j in range(check3-1):
                        spirala[check2].append(liczby[0])
                        del liczby[0]
                    for j in range(check2+1, check):
                        spirala[j].append(liczby[0])
                        del liczby[0]
                if check2 != 0:
                    for j in range(check3-1):
                        spirala[check2].insert(-check2, liczby[0])
                        del liczby[0]
                    for j in range(check2+1, check):
                        spirala[j].insert(-check2, liczby[0])
                        del liczby[0]
                check -= 1
                check2 += 1
                check3 -= 2
        return spirala
    else:
        print('Wpisz liczbę parzystą!')