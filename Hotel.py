# Declaração de variáveis para hóspede;

hospede_1 = ""
entrada_1 = ""
local_1 = 0
saida_1 = ""

hospede_2 = ""
entrada_2 = ""
local_2 = 0
saida_2 = ""

hospede_3 = ""
entrada_3 = ""
local_3 = 0
saida_3 = ""

hospede_4 = ""
entrada_4 = ""
local_4 = 0
saida_4 = ""

hospede_5 = ""
entrada_5 = ""
local_5 = 0
saida_5 = ""

#Variaveis para os quartos disponíveis;

quarto_1 = "disponivel"
quarto_2 = "disponivel"
quarto_3 = "disponivel"
quarto_4 = "disponivel"
quarto_5 = "disponivel"

# Iniciando contador para while; 
x = 1

# while para menu de opções;
while x != 0:
    print("---MENU DE OPÇÕES---")
    print("1. Cadastro de hóspede.")
    print("2. Consulta de quartos disponveís.")
    print("3. Registro de entrada e saída.")
    print("4. Listagem de hóspedes cadastrados.")
    print("5. Sair.")
    x = int(input("Escolha a opção: "))

    # if para cadastro de hóspede;
    if x == 1:

        #Variável para o alocamento dos quartos;
        y = 0
        while y != 1:
            if quarto_1 == "disponivel":
                hospede_1 = str(input("Digite o nome do hóspede: "))
                local_1 = 1
                entrada_1 = str(input("Digite o dia da entrada:"))
                saida_1 = str(input("Digite o dia da saida: "))
                quarto_1 = "indisponivel"
                y = 1

            if y != 1 and quarto_2 == "disponivel":
                nome2 = str(input("Digite o nome do hóspede: "))
                local_2 = 2
                entrada_2 = str(input("Digite o dia da entrada:"))
                saida_2 = str(input("Digite o dia da saida: "))
                quarto_2 = "indisponivel"
                y = 1

            if y != 1 and quarto_3 == "disponivel":
                nome3 = str(input("Digite o nome do hóspede: "))
                local_3 = 3
                entrada_3 = str(input("Digite o dia da entrada:"))
                saida_3 = str(input("Digite o dia da saida: "))
                quarto_3 = "indisponivel"
                y=1

            if y != 1 and quarto_4 == "disponivel":
                nome4 = str(input("Digite o nome do hóspede: "))
                local4 = 2
                entrada4 = str(input("Digite o dia da entrada:"))
                saida4 = str(input("Digite o dia da saida: "))
                quarto4 = "indisponivel"
                y = 1

            if y != 1 and quarto_5 == "disponivel":
                nome5 = str(input("Digite o nome do hóspede: "))
                local_5 = 2
                entrada_5 = str(input("Digite o dia da entrada:"))
                saida_5 = str(input("Digite o dia da saida: "))
                quarto_5 = "indisponivel"
                y = 1

        # Consultar quartos disponíveis;
        if x == 2:
            print(f"O quarto 1 esta {quarto_1}")
            print(f"O quarto 2 esta {quarto_2}")
            print(f"O quarto 3 esta {quarto_3}")
            print(f"O quarto 4 esta {quarto_4}")
            print(f"O quarto 5 esta {quarto_5}")

            # Registro de entrada e saída;
            if x == 3:
                # Variável aleatória para armazenamento de informações;
                t = int(input("Digite o numero do quarto que o hóspede esta de saida: "))

            if t == local_1:
                hospede_1 = ""
                entrada_1 = ""
                saida_1 = ""
                quarto_1 = "disponivel"
            if t == local_2:
                hospede_2 = ""
                entrada_2 = ""
                saida_2 = ""
                quarto_2 = "disponivel"
            if t == local_3:
                hospede_3 = ""
                entrada_3 = ""
                saida_3 = ""
                quarto_3 = "disponivel"
            if t == local_4:
                hospede_4 = ""
                entrada_4 = ""
                saida_4 = ""
                quarto_4 = "disponivel"
            if t == local_5:
                hospede_5 = ""
                entrada_5 = ""
                saida_5 = ""
                quarto_5 = "disponivel"

        # if para a listagem de hóspedes;
        if x == 4:
            if quarto_1 == "indisponivel":
                print(f"Nome: {hospede_1}")
                print(f"Quarto: {local_1}")
                print(f"Entrada: {entrada_1}")
                print(f"Saida: {saida_1}")

            if quarto_2 == "indisponivel":
                print(f"Nome: {hospede_2}")
                print(f"Quarto: {local_2}")
                print(f"Entrada: {entrada_2}")
                print(f"Saida: {saida_2}")

            if quarto_3 == "indisponivel":
                print(f"Nome: {hospede_3}")
                print(f"Quarto: {local_3}")
                print(f"Entrada: {entrada_3}")
                print(f"Saida: {saida_3}")
            if quarto_4 == "indisponivel":
                print(f"Nome: {hospede_4}")
                print(f"Quarto: {local_4}")
                print(f"Entrada: {entrada_4}")
                print(f"Saida: {saida_4}")
            if quarto_5 == "indisponivel":
                print(f"Nome: {hospede_5}")
                print(f"Quarto: {local_5}")
                print(f"Entrada: {entrada_5}")
                print(f"Saida: {saida_5}")
    
    # Saindo sistema.
    if x == 5:
        print("Saindo do Sistema...")
    
    else:
        print("ERROR")
