class Agente:
    def __init__(self, grafo, inicio, objetivo):
        self.grafo = grafo
        self.inicio = inicio
        self.objetivo = objetivo

    def busca_aprofundamento_iterativo(self):
        profundidade_maxima = 0

        while True:
            resultado = self.busca_profundidade_limitada(profundidade_maxima)

            if resultado is not None:
                return resultado

            profundidade_maxima += 1

    def busca_profundidade_limitada(self, profundidade_maxima):
        visitados = set()

        def busca_recursiva(estado_atual, caminho_atual, profundidade_atual):
            if profundidade_atual > profundidade_maxima:
                return None

            if estado_atual == self.objetivo:
                return caminho_atual + [estado_atual]

            visitados.add(estado_atual)

            for proximo_estado in self.grafo[estado_atual]:
                if proximo_estado not in visitados:
                    resultado = busca_recursiva(proximo_estado, caminho_atual + [estado_atual], profundidade_atual + 1)

                    if resultado is not None:
                        return resultado

            return None

        return busca_recursiva(self.inicio, [], 0)


grafo = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F'},
    'D': set(),
    'E': {'F'},
    'F': set()
}

agente = Agente(grafo, 'A', 'F')
caminho = agente.busca_aprofundamento_iterativo()

if caminho is not None:
    print('Caminho encontrado: {}'.format(caminho))
else:
    print('Não foi possível encontrar um caminho.')