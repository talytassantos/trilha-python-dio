# Função para obter o nome do mês por extenso
def obter_nome_mes(numero):
    meses = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    # Verifica se o número está no intervalo permitido
    if 1 <= numero <= 12:
        return meses[numero]
    else:
        return None

# Entrada do usuário
numero_mes = int(input("Digite um número de 1 a 12: "))

# Obtém o nome do mês por extenso
nome_mes = obter_nome_mes(numero_mes)

# Imprime o resultado
if nome_mes:
    print("O mês correspondente é:", nome_mes)
else:
    print("Número inválido. Por favor, digite um número de 1 a 12.")