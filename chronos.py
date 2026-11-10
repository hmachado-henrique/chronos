import datetime

def converter_data(data_texto):
    try:
        data_convertida = datetime.datetime.strptime(data_texto, "%d/%m/%Y").date()
        return data_convertida
    except ValueError:
        print("Formato de data inválido. Use o formato dd/mm/AAAA.")
        return None

def converter_horario(horario_texto):
    try:
        horario_convertido = datetime.datetime.strptime(horario_texto, "%H:%M").time()
        return horario_convertido
    except ValueError:
        print("Formato de horário inválido. Use o formato HH:MM.")
        return None

def calcular_horas_trabalhadas(horario_entrada, horario_saida, intervalos):
    #Converter entrada em minutos
    entrada_minutos = horario_entrada.hour * 60 + horario_entrada.minute
    #Converter saída em minutos
    saida_minutos = horario_saida.hour * 60 + horario_saida.minute
    #Calcular duração total da jornada
    duracao_total = saida_minutos - entrada_minutos
    #Percorrer os intervalos e acumular suas durações
    duracao_intervalos = 0
    for inicio, fim in intervalos:
        inicio_minutos = inicio.hour * 60 + inicio.minute
        fim_minutos = fim.hour * 60 + fim.minute
        duracao_intervalos += (fim_minutos - inicio_minutos)
    #Descontar intervalos
    duracao_trabalhada = duracao_total - duracao_intervalos
    #Retornar o total de minutos trabalhados
    return duracao_trabalhada

print("========================================")
print("      CHRONOS - CONTROLE DE JORNADA     ")
print("========================================")

while True:
    data = converter_data(input("Data (dd/mm/AAAA): "))
    if data is not None:
        break

while True:
    horario_entrada = converter_horario(input("Horário de Entrada (HH:MM): "))
    if horario_entrada is not None:
        break

intervalos = []

while True:

    # Define o horário de referência
    if not intervalos:
        horario_referencia = horario_entrada
    else:
        horario_referencia = intervalos[-1][1]

    # Solicita e valida o início do intervalo
    while True:
        inicio_intervalo = converter_horario(input("Início do Intervalo (HH:MM): "))
        if inicio_intervalo is None:
            print("Início do intervalo inválido. Digite novamente.")
            continue
        if inicio_intervalo > horario_referencia:
            break

        print("O início do intervalo deve ser posterior ao horário de referência. Digite novamente.")

    # Solicita e valida o fim do intervalo
    while True:
        fim_intervalo = converter_horario(input("Fim do Intervalo (HH:MM): "))

        if fim_intervalo is None:
            print("Fim do intervalo inválido. Digite novamente.")
            continue
        if fim_intervalo > inicio_intervalo:
            break

        print("O fim do intervalo deve ser posterior ao início do intervalo. Digite novamente.")

    intervalos.append((inicio_intervalo, fim_intervalo))

    continuar = input("Deseja adicionar outro intervalo? (S/N): ").strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input("Opção inválida. Deseja adicionar outro intervalo? (S/N): ").strip().upper()
    if continuar == 'N':
        break

# Solicita e valida o horário de saída
while True:
    horario_saida = converter_horario(input("Horário de Saída (HH:MM): "))

    if horario_saida is None:
        print("Horário de saída inválido. Digite novamente.")
        continue
    if horario_saida > intervalos[-1][1]:
        break

    print("O horário de saída deve ser posterior ao fim do último intervalo. Digite novamente.")

while True:
    observacao = input("Deseja adicionar uma observação? (S/N): ").strip().upper()
    while observacao not in ['S', 'N']:
        observacao = input("Opção inválida. Deseja adicionar uma observação? (S/N): ").strip().upper()
    if observacao == 'S':
        observacao_texto = input("Digite a observação: ")
        print(f"Observação adicionada: {observacao_texto}")
        break
    elif observacao == 'N':
        observacao_texto = ""
        break

minutos_trabalhados = calcular_horas_trabalhadas(horario_entrada, horario_saida, intervalos)
horas, minutos = divmod(minutos_trabalhados, 60)
print(f"Total de horas trabalhadas: {horas} horas e {minutos} minutos.")