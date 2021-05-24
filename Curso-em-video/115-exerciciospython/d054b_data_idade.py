from datetime import date
d1 = int(input("Em que dia vc nasceu? "))
m1 = int(input("Em que mês vc nasceu? "))
a1 = int(input("Em que ano vc nasceu? "))

d = date.today().day
m = date.today().month
a = date.today().year
if m1 < m:
    idade = a - a1
elif m1 == m:
    if d1 <= d:
        idade = a - a1
    else:
        idade = a - a1 - 1
else:
    idade = a - a1 - 1
print(f"Você tem {idade} anos.")
