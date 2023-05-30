import random

#
numero_surpresa = {1: random.randint(0, 10), 2: random.randint(0, 10), 3: random.randint(0, 10)}

#
print(numero_surpresa.values())

#
numero = random.randint(1, 10)
contador = 5

print("Jogo: Acerte o numero. Você tem 5 palpites")
print("Um numero aleatório entre 0 e 10 foi gerado")

while contador != 0:
    print("Chances:", contador)

    print(numero_surpresa.keys())
    posicao = int(input("Escolha a posicao do numero: "))

    if posicao == 1:
        palpite_01 = int(input("Digite o palpite para o numero em questão: "))
        if palpite_01 == numero_surpresa[1]:
            print("correto")
            break
        else:
            print("Incorreto")

    elif posicao == 2:
        input("Digite o palpite para o numero em questão")
    elif posicao == 3:
        input("Digite o palpite para o numero em questão")

palpite = int(input("Digite seu palpite: "))

"""if 11 < palpite < 100:
    print("Numero fora da escala imbecil!")
    print("Game Over")
    break

if palpite < numero:
    print("Errou! O numero é maior.")
    contador -= 1

elif palpite > numero:
    print("Errou! O numeor é menor")
    contador -= 1
else:
    print("Parabens voce acertou!")
    contador = 0
    break"""

if contador == 0:
    print("Voce perdeu, numeor de chances excedido")
    print("O numeor era:", numero)
