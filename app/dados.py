from .modelos import Perfil

class Carreira:
    def __init__(self, nome: str, requisitos: dict):
        self.nome = nome
        self.requisitos = requisitos

CARREIRAS = [
    Carreira("Desenvolvedor Python", {"Python": 3, "Lógica": 2}),
    Carreira("Cientista de Dados", {"Python": 3, "Estatística": 3, "Machine Learning": 2}),
    Carreira("Analista de Sistemas", {"Lógica": 3, "Modelagem de Dados": 2}),
    Carreira("Engenheiro de Software", {"Python": 4, "Arquitetura de Software": 3}),
    Carreira("Especialista em IA", {"Machine Learning": 4, "Python": 4, "Redes Neurais": 3}),
]
