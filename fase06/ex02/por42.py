def por42(num1,num2):
    num_42 = 0
    condicional = 0
    x = num2-num1
    if (x > 42):
        while condicional == 0:
            if (num1 >= num2):
                condicional += 1
            if (num1 % 42 == 0):
                num_42 += 1
                num1 += 1
            else:
                num1 += 1
            if (num_42 == 2):
                return num1 - 1
                condicional += 1
    else:
        print("Não encontrado")
        return False