#Sugerir as coordenadas dos 3 pontos que formam o tipo de triângulo escolhido pelo usuário.

opc = input("Escolha o opc de triângulo (equilatero, isoceles, escaleno): ").lower()

if opc == "equilatero":
    pontos = [(0, 0), (2, 0), (1, 1.73)]
    print("Coordenadas sugeridas:", pontos)

elif opc == "isoceles":
    pontos = [(0, 0), (2, 0), (1, 2)]
    print("Coordenadas sugeridas:", pontos)

elif opc == "escaleno":
    pontos = [(0, 0), (3, 0), (2, 4)]
    print("Coordenadas sugeridas:", pontos)

else:
    print("opc inválido")
