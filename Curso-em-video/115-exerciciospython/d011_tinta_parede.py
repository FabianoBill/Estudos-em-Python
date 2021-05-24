l = float(input('Digita a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = l*h
t = a/2
print('Sua parede de {} x {}, tem {:.2f} metros quadrados de área e precisará de {:.2f} litros de tinta par pinta-la.'.format(l, h, a, t))
