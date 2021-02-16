"""Módulo responsável pela representação e manipulação lógica dos objetos
do campeonato. Contém as seguintes classes:

    * Time - o modelo de um time
    * Jogo - o modelo de um jogo/partida envolvendo dois times
"""

class Time:
    def __init__(self, nome, vitorias = 0, derrotas = 0, empates = 0,
                 gols_pro = 0, gols_contra = 0):
        self.nome = nome
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__empates = empates
        self.__gols_pro = gols_pro
        self.__gols_contra = gols_contra

        self.__calcular_pontos()
        self.__calcular_saldo_gols()

    def __calcular_pontos(self):
        self.__pontos = 3 * self.vitorias + self.empates

    def __calcular_saldo_gols(self):
        self.__saldo_gols = self.gols_pro - self.gols_contra

    @property
    def vitorias(self):
        return self.__vitorias

    @vitorias.setter
    def vitorias(self, val):
        self.__vitorias = val
        self.__calcular_pontos()

    @property
    def derrotas(self):
        return self.__derrotas

    @derrotas.setter
    def derrotas(self, val):
        self.__derrotas = val
        self.__calcular_pontos()

    @property
    def empates(self):
        return self.__empates

    @empates.setter
    def empates(self, val):
        self.__empates = val
        self.__calcular_pontos()

    @property
    def gols_pro(self):
        return self.__gols_pro

    @gols_pro.setter
    def gols_pro(self, val):
        self.__gols_pro = val
        self.__calcular_saldo_gols()

    @property
    def gols_contra(self):
        return self.__gols_contra

    @gols_contra.setter
    def gols_contra(self, val):
        self.__gols_contra = val
        self.__calcular_saldo_gols()

    @property
    def pontos(self):
        return self.__pontos

    @property
    def saldo_gols(self):
        return self.__saldo_gols

    @property
    def jogos(self):
        return self.vitorias + self.derrotas + self.empates

class Jogo:
    """
    Classe responsável por representar um jogo entre dois times e retornar
    objetos Time atualizados de acordo com os resultados do jogo.
    """
    
    def __init__(self, time1, time2, gols1, gols2):
        # Atualizar os gols a favor e contra dos dois times.
        time1.gols_pro += gols1
        time1.gols_contra += gols2
        time2.gols_pro += gols2
        time2.gols_contra += gols1

        empate = False

        # No caso de empate ou vitória do time1, considerar o time1 como
        # vencedor e o time2 como perdedor. No caso de derrota do time1,
        # o contrário se aplica.
        if gols1 >= gols2:
            self.__time_vitorioso = time1
            self.__time_perdedor = time2
            if gols1 == gols2:
                empate = True
        else:
            self.__time_vitorioso = time2
            self.__time_perdedor = time1

        # No caso de empate, tanto o time 'vitorioso' como o time 'perdedor'
        # recebem um empate. Caso contrário, o time vitorioso ganha uma
        # vitória e o time perdedor ganha uma derrota.
        if empate:
            self.__time_vitorioso.empates += 1
            self.__time_perdedor.empates += 1
        else:
            self.__time_vitorioso.vitorias += 1
            self.__time_perdedor.derrotas += 1
        

    def get_time(self, nome):
        """
        Retorna uma representação atualizada do objeto Time correspondente
        ao nome. Caso o nome não pertença a nenhum dos times, retorna None.
        """
        if self.__time_vitorioso.nome == nome:
            return self.__time_vitorioso
        if self.__time_perdedor.nome == nome:
            return self.__time_perdedor
        return None
