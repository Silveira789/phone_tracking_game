import random

numero = random.randint(1, 10)
contador = 3

print("Jogo: Acerte o numero. Você tem 3 palpites")
print("Um numero aleatório entre 0 e 10 foi gerado")

while contador != 0:
    print("Chances:", contador)
    print(numero)
    palpite = int(input("Digite seu palpite: "))

    if 11 < palpite < 100:
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
        break

    if contador == 0:
        print("Voce perdeu, numeor de chances excedido")
        print("O numeor era:",numero)




# print(help(random))
