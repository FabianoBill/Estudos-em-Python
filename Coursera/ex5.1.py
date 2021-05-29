l = int(input("digite a largura: "))
a = int(input("digite a altura: "))
L = A = 1
while A <= a:
    while L <= l:
        print("#", end="")
        L += 1
    A += 1
    L = 1
    print()
