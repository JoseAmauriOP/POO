# Identificar o tipo de geometria a partir de 4 coordenadas inseridas pelo usuário, seja quadrado ou retângulo;

import math
x1 = float(input('Digite o X do 1º ponto:'))
y1 = float(input('Digite o Y do 1º ponto:'))

x2 = float(input('Digite o X do 2º ponto:'))
y2 = float(input('Digite o Y do 2º ponto:'))

x3 = float(input('Digite o X do 3º ponto:'))
y3 = float(input('Digite o Y do 3º ponto:'))

x4 = float(input('Digite o X do 4º ponto: '))
y4 = float(input('Digite o y do 4º ponto: '))

#Calculos dos Lados
equacao1 = (x2-x1)**2 + (y2-y1)**2
Lado1 = math.sqrt(equacao1)
print(Lado1)

equacao2 = (x3-x2)**2 + (y3-y2)**2
Lado2 = math.sqrt(equacao2)
print(Lado2)

equacao3 = (x3-x4)**2 + (y3-y4)**2
Lado3 = math.sqrt(equacao3)
print(Lado3)

equacao4 = ((x1-x4)**2 + (y1-y4)**2)
Lado4 = math.sqrt(equacao4)
print(Lado4)

#Calculos das Diagonais
equacao5 = ((x3-x1)**2  + (y3-y1)**2)
print(equacao5)
diagonal1 = math.sqrt(equacao5)
print(diagonal1)

equacao6 = ((x4-x2)**2 + (y4-y2)**2)
print(equacao6)
diagonal2 = math.sqrt(equacao6)
print(diagonal2)

angulo1 = (x2-x1)*(x4-x1) + (y2-y1)*(y4-y1)
angulo2 = (x1-x2)*(x3-x2) + (y1-y2)*(y3-y2)
angulo3 = (x2-x3)*(x4-x3) + (y2-y3)*(y4-y3)
angulo4 = (x3-x4)*(x1-x4) + (y3-y4)*(y1-y4)

verif_angulo_reto = (angulo1 == 0) and (angulo2 == 0) and (angulo3 == 0) and (angulo4 == 0) 

if verif_angulo_reto and math.isclose(Lado1, Lado2) and math.isclose(Lado2,Lado3) and math.isclose(Lado1,Lado4) and (math.isclose(diagonal1,diagonal2)):
    print('Formam um quadrado')
elif verif_angulo_reto and math.isclose(Lado1,Lado3) and math.isclose(Lado2,Lado4) and math.isclose(diagonal1, diagonal2):
    print('Forma um retangulo')
else:
    print('NÃO É FORMAM UM RETANGULO OU UM QUADRADO')