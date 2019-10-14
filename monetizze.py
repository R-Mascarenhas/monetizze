

class Loteria:      #1

    _lista = list(range(1, 61))
    _qntDezenas = 0
    _resultado = 0
    _totalJogos = 0
    _Jogos = 0

    def __init__(self, qntDezenas, totalJogos):         #3
        self._qntDezenas = self.set_QntDezenas(qntDezenas)
        self._totalJogos = self.set_totalJogos(totalJogos)

    def get_QntDezenas(self):
        return self._qntDezenas
    def set_QntDezenas(self, dezena):
        if not(isinstance(dezena, int) and dezena in range(6, 11)):
            raise ValueError("Quantidade de dezenas deve estar entre 6 e 10.\nNúmero de dezenas: {}".format(dezena))
        self._qntDezenas = dezena

    def _get_resultados(self):
        return self._resultado
    def set_resultados(self, args):
        import random
        sorteio = random.sample(self._lista, 6)
        sorteio.sort()
        self._resultado = sorteio

    def get_totalJogos(self):
        return self._totalJogos
    def set_totalJogos(self, totalJogos):
        if not(isinstance(totalJogos, int) and totalJogos > 0):
            raise ValueError("Número inválido: {}".format(totalJogos))
        self._totalJogos = totalJogos

    def get_jogos(self):
        return self._Jogos
    def set_jogos(self):
        import random
        games = [random.sample(self._lista, self._qntDezenas) for i in range(self._totalJogos)]
        games = [sorted(i) for i in games]
        games.sort()
        self._Jogos = games