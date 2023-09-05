from Calculadora import Calculator as CALC

calculadora = CALC()

while True:
    print("---------------------CONVERSÃO DE BASE-------------------------")

    num = input("DIGITE SEU NUMERO: ")
    base = int(input("DIGITE A BASE DO SEU NUMERO: "))
    base_ida = int(input("DIGITE EM QUAL BASE VOCÊ QUER A CONVERSÃO: "))
    print("----------------------------------------------------------------")

    a = calculadora.BaseFor10(num,base)
   
    if a > 0:
        b = calculadora.ten_ForBase(a,base_ida)
        print(f"O NUMERO {num} NA BASE {base_ida} É = {b} ")
        
    else:
           
        b = calculadora.ten_ForBase(abs(a),base_ida)
        print(f"O NUMERO {num} NA BASE {base_ida} É = -{b} ")


    print("----------------------------------------------------------------")
    continuacao = input("DESEJA CONVERTER OUTRO NUMERO? (S/N)")
    if continuacao == 'N':
        break

while True:
    print("-------------------------OPERAÇÕES-------------------------------")
    num1 = input("DIGITE SEU NUMERO 1: ")
    base1 = int(input("DIGITE A BASE DO SEU NUMERO 1: "))
    num2 = input("DIGITE SEU NUMERO 2: ")
    base2 = int(input("DIGITE A BASE DO SEU NUMERO 2: "))

    operation = input("ESCOLHA AS OPERAÇÕES A SEGUIR: +  -  *  /")
    if operation == '+':
        calculadora.soma(num1,num2,base1,base2)
    elif operation == '-':
        calculadora.subtraçao(num1,num2,base1,base2)
    elif operation == '*':
        calculadora.multiplication(num1,num2,base1,base2)
    elif operation == '/':
        calculadora.divisao(num1,num2,base1,base2)
    else:
        print("Operação Inválida")
    continuacao = input("DESEJA OPERAR OUTROS NUMEROS? (S/N)")
    if continuacao == 'N':
        break
