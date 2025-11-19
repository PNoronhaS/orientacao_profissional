from .modelos import Perfil
from .dados import Carreira

def recomendar_carreiras(perfil: Perfil, carreiras: list, limiar: float = 0.5) -> list:
    recomendadas = []
    for carreira in carreiras:
        compatibilidade = calcular_compatibilidade(perfil, carreira)
        if compatibilidade >= limiar:
            recomendadas.append((carreira, compatibilidade))
    recomendadas.sort(key=lambda x: x[1], reverse=True)
    return recomendadas

def calcular_compatibilidade(perfil: Perfil, carreira: Carreira) -> float:
    total = len(carreira.requisitos)
    if total == 0:
        return 0.0
    pontos = 0
    for comp, nivel_req in carreira.requisitos.items():
        nivel_user = perfil.competencias.get(comp, 0)
        if nivel_user >= nivel_req:
            pontos += 1
    return pontos / total

def gerar_trilhas(perfil: Perfil, carreira: Carreira) -> dict:
    trilhas = {}
    for comp, nivel_req in carreira.requisitos.items():
        nivel_user = perfil.competencias.get(comp, 0)
        if nivel_user < nivel_req:
            trilhas[comp] = [f"Estudar {comp}", f"Praticar exercícios de {comp}", f"Fazer projeto com {comp}"]
    return trilhas

def listar_tendencias() -> list:
    return [
        "Inteligência Artificial aplicada à saúde",
        "Automação com Python em ambientes corporativos",
        "Análise de dados em tempo real",
        "Segurança cibernética com foco em IA",
        "Desenvolvimento de sistemas éticos e responsáveis",
    ]
