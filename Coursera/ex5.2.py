l = int(input("digite a largura: "))
a = int(input("digite a altura: "))
L = A = 1
while A <= a:
    if A == 1 or A == a:
        while L <= l:
            print("#", end="")
            L += 1
    else:
        while L <= l:
            if L == 1 or L == l:
                print("#", end="")
                L += 1
            else:
                print(" ", end="")
                L += 1
    A += 1
    L = 1
    print()
