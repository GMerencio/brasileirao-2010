class Time:
    def __init__(self, nome, vitorias = 0, derrotas = 0, empates = 0, gols_pro = 0, gols_contra = 0):
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
        self.__calcular_saldo_gols()

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
