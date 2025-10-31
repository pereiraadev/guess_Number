import random

print("BEM VINDO AO GUESS NUMBER DO PEREIRA!")
choice_number = input("Digite o numero teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: o numero informado nao e um valor numerico. Favor execute novamente e informe um numero!")
    quit()

random_number = random.randint(0, choice_number)

n_choice = 0

while True:
    answer_user = input("Adivinhe o numero:")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: o numero informado nao e um valor numerico. Favor informe um numero!")
        continue

    n_choice = n_choice + 1

    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto :P ,o numero e menor do que esse!!")
    else:
        print("Chutou baixo :0 ,o numero e maior do que esse!")

print("Numero de tentativas: " + str(n_choice))
    