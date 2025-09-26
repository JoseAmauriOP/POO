#Validar e refinar o algoritmo para identificar o tipo de triângulo (escaleno, isósceles ou equilátero), a partir das coordenadas de 3 pontos no plano cartesiano (X, Y);
import math
x1 = float(input('Digite o X do 1º ponto:'))
y1 = float(input('Digite o Y do 1º ponto:'))

x2 = float(input('Digite o X do 2º ponto:'))
y2 = float(input('Digite o Y do 2º ponto:'))

x3 = float(input('Digite o X do 3º ponto:'))
y3 = float(input('Digite o Y do 3º ponto:'))

equacao1 = (x2-x1)**2 + (y2-y1)**2
Lado1 = (math.sqrt(equacao1))
print(Lado1)

equacao2 = (x3-x1)**2 + (y3-y1)**2
Lado2 = (math.sqrt(equacao2))
print(Lado2)

equacao3 = (x3-x2)**2 + (y3-y2)**2
Lado3 = (math.sqrt(equacao3))
print(Lado3)

if math.isclose(Lado1,Lado2,abs_tol= 0.1) and math.isclose(Lado1,Lado3, abs_tol= 0.1) and math.isclose(Lado2,Lado3, abs_tol= 0.1):
    print('É um triangulo equilatero')
elif (math.isclose(Lado1,Lado2, abs_tol= 0.1) and Lado1 != Lado3) or (math.isclose(Lado1, Lado3, abs_tol= 0.1) and Lado1 != Lado2) or (math.isclose(Lado2, Lado3, abs_tol= 0.1) and Lado2 != Lado1): 
    print('É um triangulo isosceles')
else:
    print('É um triagulo escaleno')