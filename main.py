from model import Time, Jogo

def carregar_dados(caminho):
    """
    Retorna uma lista de objetos Time criados a partir do arquivo de texto
    cujo caminho é passado como argumento. A lista é ordenada pelo atributo
    pontos, em ordem decrescente. Cada linha do arquivo deve conter um
    resultado de partida no seguinte formato:

    DD/MM/YYYY - HH:MM - time1 AxB time2

    DD/MM/YYYY é a data, HH:MM é o horário, time1 é o primeiro time, A é
    a quantidade de gols do primeiro time, time2 é o segundo time e B é
    a quantidade de gols do segundo time.
    """
    times = {}

    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            # Desconsiderar os primeiros 21 caracteres da linha, bem como
            # espaço em branco no final.
            linha = linha.rstrip()[21:]
            print(linha)

            linha_split = linha.split(' ')

            # Desconsiderar linhas que não estiverem no formato esperado.
            if len(linha_split) != 3:
                continue

            nome1, placar, nome2 = linha_split
            gols1, gols2 = [int(gols) for gols in placar.split('x')]

            if nome1 not in times:
                times[nome1] = Time(nome1)
            if nome2 not in times:
                times[nome2] = Time(nome2)

            # Inserir os resultados em um objeto Jogo e obter os objetos Time
            # atualizados.
            jogo = Jogo(times[nome1], times[nome2], gols1, gols2)
            times[nome1] = jogo.get_time(nome1)
            times[nome2] = jogo.get_time(nome2)
    
    return sorted(times.values(), key = lambda time: time.pontos,
                  reverse = True)

tabela = carregar_dados('jogos.txt')
for time in tabela:
    print(time.nome, time.pontos)
