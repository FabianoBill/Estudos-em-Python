
# def lin():
#     print("-="*20)


# lin()

# def msg(msg):
#     print("-="*30)
#     print(f"{msg:^60}")
#     print("-="*30)


# msg("Bill")
# msg("Estudando Python")

# def soma(a, b):
#     s = a + b
#     print(f"{a} + {b} = {s}")


# soma(2, 3)
# soma(b=2, a=3)

# def contador(*n):    # parâmetro empacotado
#     print(n)


# contador(2, 1)
# contador(1, 2, 3)

def dobra(lst):
    p = 0
    while p < len(lst):
        lst[p] *= 2
        p += 1
        

lista = [1, 2, 3, 4]
dobra(lista)
print(lista)