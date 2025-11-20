from perfil import Perfil
from carreira import Carreira

# lista de competências avaliadas
COMPETENCIAS = [
    "Lógica de programação",
    "Criatividade",
    "Colaboração",
    "Adaptabilidade",
    "Pensamento crítico",
    "Comunicação",
    "Análise de dados",
    "Programação em Python"
]

# criação das carreiras (com pesos das competências)
ci_dados = Carreira(
    "Cientista de Dados",
    "Tecnologia",
    {
        "Análise de dados": 5,
        "Programação em Python": 5,
        "Lógica de programação": 4,
        "Pensamento crítico": 4,
        "Comunicação": 3
    }
)

ia_eng = Carreira(
    "Engenheira de IA",
    "Tecnologia",
    {
        "Programação em Python": 5,
        "Lógica de programação": 5,
        "Análise de dados": 4,
        "Adaptabilidade": 3
    }
)

ux = Carreira(
    "UX Designer",
    "Design digital",
    {
        "Criatividade": 5,
        "Colaboração": 4,
        "Comunicação": 4,
        "Adaptabilidade": 3
    }
)

fullstack = Carreira(
    "Desenvolvedora Full Stack",
    "Desenvolvimento de Software",
    {
        "Programação em Python": 5,
        "Lógica de programação": 5,
        "Colaboração": 4,
        "Pensamento crítico": 3,
        "Adaptabilidade": 3
    }
)

cybersec = Carreira(
    "Analista de Segurança Cibernética",
    "Cyber Security",
    {
        "Lógica de programação": 5,
        "Pensamento crítico": 5,
        "Análise de dados": 4,
        "Adaptabilidade": 4,
        "Comunicação": 2
    }
)

# entrada do nome do usuário
nome = input("Digite seu nome: ").strip()
if not nome:
    nome = "Usuário"

# instruções de avaliação
print("=====================================\n")
print("Avalie suas competências de 0 a 5:\n")
print("0 = nenhum conhecimento")
print("1 = muito básico")
print("2 = início do aprendizado")
print("3 = intermediário")
print("4 = bom")
print("5 = avançado\n")
print("=====================================\n")

competencias_usuario = {}

# coleta das notas do usuário
for comp in COMPETENCIAS:
    val = int(input(f"{comp}: "))
    competencias_usuario[comp] = val

# cria o perfil
perfil1 = Perfil(nome, competencias_usuario)

# adiciona as carreiras 
perfil1.adicionar_carreira(ci_dados)
perfil1.adicionar_carreira(ia_eng)
perfil1.adicionar_carreira(ux)
perfil1.adicionar_carreira(fullstack)
perfil1.adicionar_carreira(cybersec)

# exibe o relatório final
perfil1.exibir_relatorio()
