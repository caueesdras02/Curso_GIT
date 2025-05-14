n1 = int(input("Insira o 1° número desejado: "))
n2 = int(input("Insira o 2° número desejado: "))
op1 = n1 * n2
op2 = n1 + n2
op3 = n1 - n2
n3 = str(input("\n op1 = * \n op2 = + \n op3 = - \n \n Insira a operação desejada: "))
if n3 == "op1":
    print(f"\nA nultiplicação dos números é: {op1}")
elif n3 == "op2":
    print(f"\nA soma dos números é: {op2}")
elif n3 == "op3":
    print(f"\nA subtração dos números é: {op3}")
else: 
    print("ERRO!!! SELECIONE UMA DAS OPÇÕES!")