import random

num_secreto = random.randint(1, 100) # Gera um número aleatório entre 1 e 100
num_tentativas = 0
max_tentativas = 7 # Define o limite máximo de palpites

print("Bem-vindo ao jogo Adivinhe o Número!")
print(f"Eu escolhi um número entre 1 e 100. Você tem {max_tentativas} tentativas para adivinhar.")

while num_tentativas < max_tentativas:
    num_tentativas += 1
    num_chute = int(input("Digite um número: "))

    if num_chute < num_secreto:
        print("O número é maior. Tente novamente.")
    elif num_chute > num_secreto:
        print("O número é menor. Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número em {num_tentativas} tentativas.")
        break

if num_tentativas == max_tentativas:
    print(f"Suas {max_tentativas} tentativas acabaram. O número secreto era {num_secreto}. Tente novamente!")