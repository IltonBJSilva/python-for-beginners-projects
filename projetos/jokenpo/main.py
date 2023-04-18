 # Importa a bibliotecas
import random


user_point = 0; # Pontuação do usuário
computer_point = 0; # Pontuação do computador


while True:
    # Entrada de dados
    user = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q/N para sair \nDigite sua jogada: ").lower() # Transforma a entrada em minúsculo
    computer = random.choice(["r", "p", "t"]) # Escolhe aleatoriamente entre r, p e t


    # Pergunta se o usuário quer jogar novamente
    if user == "n" or user == "q":
        break

    # Processamento
    if user == computer:
        print("Empate!")
    # Se o usuário escolher pedra
    elif user == "r":
        # Se o computador escolher tesoura
        if computer == "t":
            print("Você ganhou!")
            user_point += 1
        # Se o computador escolher papel
        else:
            print("Você perdeu!")
            computer_point += 1
    # Se o usuário escolher papel
    elif user == "p":
        # Se o computador escolher pedra
        if computer == "r":
            print("Você ganhou!")
            user_point += 1
        # Se o computador escolher tesoura
        else:
            print("Você perdeu!")
            computer_point += 1
    # Se o usuário escolher tesoura
    elif user == "t":
        # Se o computador escolher pedra
        if computer == "p":
            print("Você ganhou!")
            user_point += 1
        # Se o computador escolher papel
        else:
            print("Você perdeu!")
            computer_point += 1
    # Se o usuário digitar uma jogada inválida
    else:
        print("Jogada inválida!")

    # Saída de dados
    print(f"Você: {user_point} x {computer_point} :Computador")
    print(f'Criado por Ilton Batista')