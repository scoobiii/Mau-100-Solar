import os

# Define a estrutura de pastas e arquivos
estrutura = {
    "MauáThonSprint-1/": [],
    "MauáThonZero/": [],
    "PerGen/": ["README.md"],
    "Pré-MauáThon/": ["README.md"],
    "Documentação/Contrato/Anexos/": [
        "Cronograma_Financeiro.xlsx",
        "Cronograma_Físico.xlsx",
        "Termos_Referência.md",
    ],
    "Documentação/Contrato/": ["Contrato_Principal.md", "Smart_Contract.sol"],
    "Documentação/Relatórios/": [
        "Relatório_Impacto_Anual_2024.pdf",
        "Relatório_Final_2030.pdf",
    ],
    "Documentação/": ["Plano_Projeto.md"],
    "Planejamento/Estratégia/": [],
    "Planejamento/KPIs/": [],
    "Planejamento/": ["Plano_Execução.md"],
    "Mobilização/Campanhas/": [],
    "Mobilização/Eventos_Preparatorios/": [],
    "Mobilização/Relatórios_Engajamento/": [],
    "Execução/Edições/": [],
    "Execução/Infraestrutura_Evento/": [],
    "Execução/Resultados/": [],
    "Monitoramento/Relatórios_Anuais/": [],
    "Monitoramento/Avaliação_Impacto/": [],
    "": ["README.md"],
}

# Cria a estrutura de pastas e arquivos
def criar_estrutura(base_path, estrutura):
    for pasta, arquivos in estrutura.items():
        caminho_completo = os.path.join(base_path, pasta)
        os.makedirs(caminho_completo, exist_ok=True)
        for arquivo in arquivos:
            with open(os.path.join(caminho_completo, arquivo), "w") as f:
                f.write("")  # Cria o arquivo vazio

# Defina o caminho base (onde o projeto será criado)
base_path = "MauáThon"

# Executa a criação da estrutura
criar_estrutura(base_path, estrutura)

print(f"Estrutura do projeto criada em: {os.path.abspath(base_path)}")
