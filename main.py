#problema 2
def get_prim(p):
    '''Verifica daca numarul este prim
    :param :p intreg
    :return: True daca este prim sau False daca nu
    '''
    if p<2:
        return 0
    else:
        for div in range(2,p//2+1):
            if p%div==0:
                return 0
    return 1


def test_get_prim():
    assert get_prim(3)==1
    assert get_prim(6)==0


def get_longest_all_primes(lst):
    '''
    Determinarea secventa cea mai lunga cu prop ca nr sunt prime
    :param lst: lista de nr intregi
    :return: rez lista care reprezinta secventa de lungime maxima
    cu prop ca nr sunt prime
    '''
    rez = []  # rezultatul final
    temp = []  # solutia curenta
    for x in lst:  # foreach
        if get_prim(x)==1:
            temp.append(x)
        else:
            if (len(temp) > len(rez)):
                rez = temp[:]
            temp.clear()
    if (len(temp) > len(rez)):
        rez = temp[:]
    return rez


def test_get_longest_all_primes ():
    assert get_longest_all_primes([3, 5, 7, 9,11])==[3,5,7]
    assert get_longest_all_primes([3,11,13,12,11,11,11,13,13,13])==[11,11,11,13,13,13]


#problema 13
def get_cif_prim(n):
    '''testeaza daca un numar este format doar din cifre prime
    :param: n numar intreg
    :return: 1 daca toate cifrele sunt prime si 0 in rest
    '''
    while n!=0:
        uc=n%10
        if get_prim(uc)==0:
            return 0

        n=n//10
    return 1


def test_get_cif_prim():
    assert get_cif_prim(12)==0
    assert  get_cif_prim(123)==0
    assert  get_cif_prim (1)==0
    assert get_cif_prim(357) == 1


def get_longest_prime_digits(lst):
    '''Determina secventa cea mai lunga cu proprietatea ca toate cifrele numerelor sunt pime
    :param: lst
    :return: rez :lista cu proprietatea anuntata mai sus'''
    rez = []  # rezultatul final
    temp = []  # solutia curenta
    for x in lst:  # foreach
        if get_cif_prim(x)==1:
            temp.append(x)
        else:
            if (len(temp) > len(rez)):
                rez = temp[:]
            temp.clear()
    if (len(temp) > len(rez)):
        rez = temp[:]
    return rez



def test_get_longest_prime_digits():
    assert get_longest_prime_digits([23,235,35,4,12,35])==[23,235,35]
    assert get_longest_prime_digits([77,23,65,55])==[77,23]

def meniu():
    print("""
1.Citire date
2.Determinarea celei mai lungi secvente cu proprietatea de la pb 2
3.Determinarea celei mai lungi secvente cu proprietatea de la pb 18
4.Iesire""")


def citire(n):
    lst=[]
    for i in range(0,n):
        p=int(input("introduceti elemntul"))
        lst.append(p)
    return lst


def teste():
    test_get_prim()
    test_get_cif_prim()
    test_get_longest_all_primes()
    test_get_longest_prime_digits()


def main():
    lst=[]
    teste()
    while True:
        meniu()
        cmd=int(input("introduceti comanda"))
        if cmd==1:
            n=int(input("cate numere sa fie in lista?"))
            lst=citire(n)
        elif cmd==2:
            print(get_longest_all_primes(lst))
        elif cmd==3:
            print(get_longest_prime_digits(lst))
        elif cmd==4:
            break
        else:
            print("comanda invalida")


if __name__ == '__main__':main()







