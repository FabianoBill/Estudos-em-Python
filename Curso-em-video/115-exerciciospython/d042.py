a = float(input('Medida do lado 1: '))
b = float(input('Medida do lado 2: '))
c = float(input('Medida do lado 3: '))
if a < b + c and b < a + c and c < a + b:
    print('Com essas medidas é possível formar um triangulo ', end='')
    if a != b != c:
        print('escaleno.')
    elif a == b == c:
        print('equilátero.')
    else:
        print('isósceles.')
else:
    print('É impossível formar um tiângulo com essas medidas.')
