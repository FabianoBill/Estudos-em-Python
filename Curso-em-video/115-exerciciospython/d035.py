a = float(input('Digite o comprimento do seguimento de reta a: '))
b = float(input('Digite o comprimento do seguimento de reta b: '))
c = float(input('Digite o comprimento do seguimento de reta c: '))

if a < b + c and b < a + b and c < a + b:
    print('É possível formar um triângulo com essas medidas.')
else:
    print('É ipossível formar um triângulo com essas medidas.')
