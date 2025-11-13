# Classe que representa uma carreira profissional
class Carreira:
    def __init__(self, nome, area, pesos):
        self.nome = nome
        self.area = area
        self.pesos = pesos

    def exibir_informacoes(self):
        # mostra o nome e a área da carreira
        print(f"Carreira: {self.nome} | Área: {self.area}")
        print("Competências relevantes e pesos:")
        for comp, peso in self.pesos.items():
            print(f"  {comp}: peso {peso}")
