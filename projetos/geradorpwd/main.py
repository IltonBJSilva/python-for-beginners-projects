import random
import string 

def password_generator(len_pass = 8, type_pass = 1):
    ascii_option = string.ascii_letters
    number_option = string.digits
    punt_option = string.punctuation


    password_user = ""

    if type_pass == 1:
        option = number_option
    elif type_pass == 2:
        option = ascii_option
    elif type_pass == 3:
        option = ascii_option + number_option
    elif type_pass == 4:
        option = ascii_option + number_option + punt_option
    else:
        print('Opção inválida')
        quit()

    for i in range(0, len_pass):
        digit = random.choice(option)
        password_user = password_user + digit
    return password_user





while True:
    pwd = input('Digite a quantidade de caracteres da senha: ')
    choice_type = input('Digite o tipo de senha: \n 1 - Números \n 2 - Letras \n 3 - Números e Letras \n 4 - Números, Letras e Caracteres Especiais \n')

    if pwd.isdigit() and choice_type.isdigit():
        pwd = int(pwd)
        choice_type = int(choice_type)
    else:
        print('Digite apenas números')
        quit()


    response = password_generator(len_pass=pwd, type_pass=choice_type)
    print(f"Senha gerada: {response}")

    if input('Deseja gerar outra senha? (S/N) ').upper() == 'N':
        break