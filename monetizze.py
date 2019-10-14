

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

    def get_totalJogos(self):
        return self._totalJogos
    def set_totalJogos(self, totalJogos):
        if not(isinstance(totalJogos, int) and totalJogos > 0):
            raise ValueError("Número inválido: {}".format(totalJogos))
        self._totalJogos = totalJogos
        return self._totalJogos

    def _get_array(self, qntDezenas):       #4
        import random
        sorteio = random.sample(self._lista, qntDezenas)
        sorteio.sort()
        self._array = sorteio
        return self._array

    def get_resultados(self):
        return self._resultado
    def set_resultados(self):
        self._resultado = self._get_array(6)
        return self._resultado


    def get_jogos(self):
        return self._Jogos
    def set_jogos(self):                #5
        games = [self._get_array(self._qntDezenas) for i in range(self._totalJogos)]
        game_unique = [list(x) for x in set(tuple(x) for x in games)]
        if not(len(game_unique) == len(games)):
            self.set_jogos()

        games.sort()
        self._Jogos = games
        return self._Jogos

    def get_Confere(self):

        results = []

        for i in range(self._totalJogos):
            acertos = [num for num in self._Jogos[i] if num in self._resultado]
            results.append(len(acertos))

        HTML = ""
        HTML = HTML + "<html><head><title>Resultados Loteria</title></head><body><h2>Loteria</h2><h4>Resultado do sorteio: "
        HTML = HTML + str(self._resultado)
        HTML = HTML + "<table border = 0>"
        HTML = HTML + "<br /><br /><tr><td><h4>Jogos</td><td><h4>Dezenas sorteadas</td></tr><br /><br />"
        for i in range(self._totalJogos):
            HTML = HTML + "<tr>"
            HTML = HTML + "<td>" + str(self._Jogos[i]) + "</td>"
            HTML = HTML + "<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + str(results[i]) + "</td>"
            HTML = HTML + "</tr>"
        HTML = HTML + "</table></body></html>"
        f = open('monetizze_resultado.html', 'w')
        f.writelines(HTML.strip(("[]")))
        f.close()
        import webbrowser
        webbrowser.open("monetizze_resultado.html", new = 2)
        return HTML.strip("[]")



dezenas = int(input("Informe o número de dezenas entre 6 e 10: "))
jogos = int(input("Informe o número de Jogos: "))
loteca = Loteria(dezenas, jogos)
loteca.set_resultados()
loteca.set_jogos()
loteca.get_Confere()



