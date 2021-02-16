from model import Time, Jogo

def carregar_dados(arquivo):
    """
    Retorna uma lista de objetos Time criados a partir do arquivo de texto
    passado como argumento. A lista é ordenada pelo atributo pontos, em ordem
    decrescente. Cada linha do arquivo deve conter um resultado de partida
    no seguinte formato:

    DD/MM/YYYY - HH:MM - time1 AxB time2

    DD/MM/YYYY é a data, HH:MM é o horário, time1 é o primeiro time, A é
    a quantidade de gols do primeiro time, time2 é o segundo time e B é
    a quantidade de gols do segundo time.
    """
    times = {}
    times['Corint'] = Time('Corint', 4, 1, 1)
    times['Palm'] = Time('Palm', 10, 0, 0)
    return sorted(times.values(), key = lambda time: time.pontos,
                  reverse = True)

tabela = carregar_dados('jogos.txt')
for time in tabela:
    print(time.nome, time.pontos)
