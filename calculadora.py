# função para verificar se uma string é um número (tanto inteiro, negativo ou real)
def isnumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True


while True:

    print('************************************** Python Calculator **************************************')
    print('Selecione o número da operação desejada:')
    print('\n1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão\n')

    try:
        opcao = input('Digite sua opção (1/2/3/4): ')
        if not isnumber(opcao) or int(opcao) < 1 or int(opcao) > 4:
            print('Escolha uma opção válida!\n')
            continue
    except ValueError:
        print('Escolha uma opção válida!\n')
        continue

    while True:
        op1 = input('\nDigite o primeiro número: ')
        if not isnumber(op1):
            print('Digite apenas números!')
            continue
        break

    while True:
        op2 = input('\nDigite o segundo número: ')
        if not isnumber(op2):
            print('Digite apenas números!')
            continue
        break

    if opcao == '1':
        soma = float(op1) + float(op2)
        print('\n{0} + {1} = {2}'.format(op1, op2, soma))
        break

    if opcao == '2':
        sub = float(op1) - float(op2)
        print('\n{0} - {1} = {2}'.format(op1, op2, sub))
        break

    if opcao == '3':
        mul = float(op1) * float(op2)
        print('\n{0} * {1} = {2}'.format(op1, op2, mul))
        break

    if opcao == '4':
        try:
            div = float(op1) / float(op2)
            print('\n{0} / {1} = {2}'.format(op1, op2, div))
            break
        except ZeroDivisionError:
            print('Não é possível divisão por zero!\n')
            continue
