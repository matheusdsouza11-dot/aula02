import random

numero_secreto = random.randint(1, 10)
palpite = int(input("Chute um número de 1 a 10: "))
print(f"Você {'acertou' if palpite == numero_secreto else 'errou'}. O número era {numero_secreto}!")
