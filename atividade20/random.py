# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM

import random
numero_aleatorio = random.radint(0, 5)
numero_usuario = int(input("tente adivinha o numero escolhido entre 0 e 5: "))
if numero_usuario == numero_aleatorio:
    print("acertou")
else:
    print(f"errou, numero correto era {numero_aleatorio}")