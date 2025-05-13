print('Você deseja digitar o numero o numero em qual base?')

base_inicial = input('Escolha [D]ecimal, [H]exadecimal, [B]inario ou [O]ctal: ')

numero_inicial = input('Digite o número: ')

conversao_base = input('Escolha a base para conversão [D]ecimal, [H]exadecimal, [B]inario ou [O]ctal: ')

if base_inicial == 'D' or base_inicial == 'd':
    numero_decimal = int(numero_inicial)
    if conversao_base == 'H' or conversao_base == 'h':
        print(f'O Hexadecimal de {numero_decimal} é {numero_decimal:x}')

    elif conversao_base == 'B' or conversao_base == 'b':
        print(f'O Binário de {numero_decimal} é {bin(numero_decimal)[2:]}')

    elif conversao_base == 'O' or conversao_base == 'o':
        print(f'O Octal de {numero_decimal} é {oct(numero_decimal)[2:]}')

if base_inicial == 'H' or base_inicial == 'h':

    numero_hexadecimal = int(numero_inicial, 16)

    if conversao_base == 'D' or conversao_base == 'd':
        print(f'O Decimal de {numero_inicial} é {numero_hexadecimal:d}')

    elif conversao_base == 'B' or conversao_base == 'b':
        print(f'O Binário de {numero_hexadecimal} é {bin(numero_hexadecimal)[2:]}')

    elif conversao_base == 'O' or conversao_base == 'o':
        print(f'O Octal de {numero_hexadecimal} é {oct(numero_hexadecimal)[2:]}')

if base_inicial == 'B' or base_inicial == 'b':

    numero_binario = int(numero_inicial, 2)

    if conversao_base == 'D' or conversao_base == 'd':
        print(f'O Decimal de {numero_inicial} é {numero_binario:d}')

    elif conversao_base == 'H' or conversao_base == 'h':
        print(f'O Hexadecimal de {numero_binario} é {hex(numero_binario)[2:]}')

    elif conversao_base == 'O' or conversao_base == 'o':
        print(f'O Octal de {numero_binario} é {oct(numero_binario)[2:]}')
        
elif base_inicial == 'O' or base_inicial == 'o':

    numero_octal = int(numero_inicial, 8)

    if conversao_base == 'D' or conversao_base == 'd':
        print(f'O Decimal de {numero_inicial} é {numero_octal:d}')

    elif conversao_base == 'H' or conversao_base == 'h':
        print(f'O Hexadecimal de {numero_octal} é {hex(numero_octal)[2:]}')

    elif conversao_base == 'B' or conversao_base == 'b':
        print(f'O Binário de {numero_octal} é {bin(numero_octal)[2:]}')
        
