import time, sys

entrada = input("Digite o tempo em segundos: ")

if entrada.isdigit():
    while True:
        entrada = int(entrada)

        for i in range(0, entrada):
            contador = i+1

            print(contador)
            time.sleep(1)

        print ("\nFim")
        
        if contador >= entrada:
            break

        
    else:
        print("Digite um número inteiro")
        
'''
# Path: projetos\temporizador\main.py

temporizador simples em python 3 com o módulo time e sys para sair do programa com o comando sys.exit() 


'''

