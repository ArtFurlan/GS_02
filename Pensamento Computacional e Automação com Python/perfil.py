from carreira import Carreira

# Classe que representa o perfil do usuário
class Perfil:
    def __init__(self, nome, competencias):
        self.nome = nome
        self.competencias = competencias
        self.carreiras = []
        self.compatibilidade_por_carreira = {}

    def adicionar_carreira(self, carreira: Carreira):
        # adiciona carreira à lista, caso não esteja
        if carreira not in self.carreiras:
            self.carreiras.append(carreira)
        self.compatibilidade_por_carreira.setdefault(carreira.nome, 0)

    def calcular_compatibilidade(self, carreira: Carreira):
        # calcula compatibilidade baseado nos pesos e nas notas informadas
        pesos = carreira.pesos
        total_pesos = sum(pesos.values())
        score = 0

        for comp, peso in pesos.items():
            nivel = self.competencias.get(comp, 0)
            score += (nivel / 5) * peso

        compat = (score / total_pesos) * 100
        self.compatibilidade_por_carreira[carreira.nome] = compat
        return compat

    def melhor_carreira(self):
        # encontra a carreira de maior compatibilidade
        if not self.carreiras:
            return None
        melhor = None
        maior = -1
        for carreira in self.carreiras:
            compat = self.calcular_compatibilidade(carreira)
            if compat > maior:
                maior = compat
                melhor = carreira
        return melhor, maior

    def exibir_relatorio(self):
        print(f"\nPerfil: {self.nome}")
        print("Competências do perfil:")
        for comp, nivel in self.competencias.items():
            print(f"  {comp}: {nivel}")

        if not self.carreiras:
            print("\nNenhuma carreira associada a este perfil.")
            return

        print("\nCarreiras avaliadas:")
        resultados = []

        # calcula compatibilidade de todas as carreiras
        for carreira in self.carreiras:
            carreira.exibir_informacoes()
            compat = self.calcular_compatibilidade(carreira)
            resultados.append((carreira, compat))
            print(f"  Compatibilidade: {compat:.1f}%\n")

        # encontra maior porcentagem
        maior = max(score for _, score in resultados)

        # lista de carreiras empatadas no maior valor
        melhores = [(c, s) for c, s in resultados if s == maior]

        print("Melhor(es) carreira(s) para você:")
        for carreira, score in melhores:
            print(f" - {carreira.nome} ({score:.1f}%)")

        # mensagem final de orientação
        print("Antes de escolher, avalie cuidadosamente cada área e pesquise mais profundamente para decidir, por conta própria, se a opção (ou as opções) realmente faz sentido para seus objetivos.")
