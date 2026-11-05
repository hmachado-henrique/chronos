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

print("========================================")
print("      CHRONOS - CONTROLE DE JORNADA     ")
print("========================================")

while True:
    data = converter_data(input("Data (dd/mm/AAAA): "))
    if data is not None:
        break

while True:
    horario = converter_horario(input("Horário de Entrada (HH:MM): "))
    if horario is not None:
        break

intervalos = []

while True:
    while True:
        inicio_intervalo = converter_horario(input("Início do Intervalo (HH:MM): "))
        if inicio_intervalo is not None:
            break
        else:
            print("Intervalo inválido. Digite novamente.")
    while True:
        fim_intervalo = converter_horario(input("Fim do Intervalo (HH:MM): "))
        if fim_intervalo is not None:
            break
        else:
            print("Fim do intervalo inválido. Digite novamente.")

    intervalos.append((inicio_intervalo, fim_intervalo))

    continuar = input("Deseja adicionar outro intervalo? (S/N): ").upper()
    if continuar != 'S':
        break
