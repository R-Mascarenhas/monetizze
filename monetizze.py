

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
        return self._qntDezenas


    def _get_array(self, qntDezenas):       #4
        import random
        sorteio = random.sample(self._lista, qntDezenas)
        sorteio.sort()
        self._array = sorteio
        return self._array

    def get_resultados(self):
        return self._resultado
    def set_resultados(self, args):
        self._resultado = self._get_array(6)
        return self._resultado

    def get_totalJogos(self):
        return self._totalJogos
    def set_totalJogos(self, totalJogos):
        if not(isinstance(totalJogos, int) and totalJogos > 0):
            raise ValueError("Número inválido: {}".format(totalJogos))
        self._totalJogos = totalJogos
        return self._totalJogos

    def get_jogos(self):
        return self._Jogos
    def set_jogos(self):                #5 FALTA UNIQUE
        import random
        games = [self._get_array(self._qntDezenas) for i in range(self._totalJogos)]
        games = [sorted(i) for i in games]
        games.sort()
        self._Jogos = games
        return self._Jogos

    def get_Confere(self):

        results = []

        for i in range(self._totalJogos):
            acertos = [num for num in self._Jogos[i] if num in self._resultado]
            results.append(len(acertos))

        print("\nNúmeros sorteados: " + str(self._resultado))
        print("\nNúmeros apostados: " + " " * self._totalJogos * 3 + "Acertos:\n")
        for i in range(self._totalJogos):
            jogo = sorted(self._Jogos[i])
            print(str(jogo) + "       \t\t" + str(results[i]))

        return results


loteca = Loteria(10, 30)
loteca.set_resultados(1)
loteca.set_jogos()
loteca.get_Confere()
