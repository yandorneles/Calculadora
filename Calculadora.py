while True:
    print("\n"+"Escolha uma operação:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Divisão Inteira\n6 - Módulo\n7 - Potenciação\n0 - Sair")

    oper = int (input("Informe o número da operação: "))

    while oper > 7 or oper < 0:
        oper = int (input("Não existe essa operação, indique uma operação entre 0 e 7: "))
        
    if(oper == 0):
        print("Saindo")
        break   
     
    a = float (input("Informe o primeiro número: "))

    b = float (input("Informe o segundo número: "))
    
    match oper:
        case 1:
            resul = a + b
            print("O resultado é: "+str(resul))
        case 2:
            resul = a - b
            print("O resultado é: "+str(resul))
        case 3:
            resul = a * b
            print("O resultado é: "+str(resul))
        case 4:
            while b == 0:
                 print("Não existe divisão por zero.")
                 b = float(input("Informe o segundo número novamente: "))
            resul = a / b
            print("O resultado é: "+str(resul))
        case 5:
            resul = a // b
            print("O resultado é: "+str(resul))
        case 6:
            resul = a % b
            print("O resultado é: "+str(resul))
        case 7:
            resul = a ** b
            print("O resultado é: "+str(resul))