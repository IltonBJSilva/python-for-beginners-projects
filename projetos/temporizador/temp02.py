import time, sys

# Função para imprimir o tempo restante
t = input ("Digite o tempo em (segundos): ")

# Verifica se o valor digitado é um número inteiro
if t.isdigit:
    # Converte o valor digitado para inteiro
    t = int(t)
    # Inicia o temporizador
    print("Temporizador iniciado")
# Se o valor digitado não for um número inteiro
else:
    # Exibe a mensagem de erro
    print("Digite um valor inteiro")
    # Encerra o programa
    sys.exit()

# Enquanto o tempo for maior que zero
while t: # 0 --> False, 1 --> True
    # Converte o tempo em segundos para horas, minutos e segundos
    minutes, seconds = divmod(t, 60) # Retorna o quociente e o resto da divisão
    # Formata o tempo para exibição
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    # Imprime o tempo restante sobescrevendo o anterior
    print(timer, end="\r")
    t = t-1
    time.sleep(1)

print('TEMPO ACABOU!!!!')