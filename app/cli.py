from .modelos import Perfil
from .dados import CARREIRAS
from .servicos import recomendar_carreiras, gerar_trilhas, listar_tendencias
from .persistencia import salvar_perfil, carregar_perfil, gerar_relatorio_pdf

def coletar_perfil() -> Perfil:
    print("\n=== Criação de Perfil ===")
    nome = input("Seu nome: ").strip() or "Usuário"
    competencias_usuario = {}
    print("Digite suas competências e níveis (1-5). Digite 'fim' para encerrar.")
    while True:
        comp = input("Competência: ").strip()
        if comp.lower() == "fim":
            break
        try:
            nivel = int(input("Nível (1-5): "))
            if 1 <= nivel <= 5:
                competencias_usuario[comp] = nivel
            else:
                print("Digite um número entre 1 e 5.")
        except ValueError:
            print("Digite um número válido.")
    perfil = Perfil(nome, competencias_usuario)
    salvar_perfil(perfil)
    return perfil

def mostrar_recomendacoes(perfil: Perfil):
    print(f"\n=== Recomendações de Carreira para {perfil.nome} ===")
    recomendadas = recomendar_carreiras(perfil, CARREIRAS, limiar=0.5)
    if not recomendadas:
        print("Nenhuma carreira atingiu o limiar mínimo de compatibilidade (>= 50%).")
        return []
    for carreira, compat in recomendadas:
        porcent = int(compat * 100)
        print(f"- {carreira.nome}: compatibilidade {porcent}%")
        trilhas = gerar_trilhas(perfil, carreira)
        if trilhas:
            print("  Lacunas e trilhas sugeridas:")
            for comp, etapas in trilhas.items():
                print(f"    * {comp}:")
                for etapa in etapas:
                    print(f"      - {etapa}")
        else:
            print("  Você atende aos requisitos principais desta carreira!")
    return recomendadas

def mostrar_tendencias():
    print("\n=== Tendências de Carreira ===")
    tendencias = listar_tendencias()
    for t in tendencias:
        print(f"- {t}")
    return tendencias

def menu():
    perfil = carregar_perfil()
    while True:
        print("\n===============================")
        print("SISTEMA DE ORIENTAÇÃO PROFISSIONAL")
        print("===============================")
        print("1. Criar/Atualizar meu perfil")
        print("2. Ver recomendações de carreira")
        print("3. Ver tendências futuras")
        print("4. Sair")
        print("5. Gerar relatório em PDF")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            perfil = coletar_perfil()
        elif opcao == "2":
            if perfil is None:
                print("Crie seu perfil primeiro (opção 1).")
            else:
                recomendacoes = mostrar_recomendacoes(perfil)
        elif opcao == "3":
            mostrar_tendencias()
        elif opcao == "4":
            print("Até a próxima!")
            break
        elif opcao == "5":
            if perfil is None:
                print("Crie seu perfil primeiro (opção 1).")
            else:
                recomendacoes = recomendar_carreiras(perfil, CARREIRAS, limiar=0.5)
                tendencias = listar_tendencias()
                gerar_relatorio_pdf(perfil, recomendacoes, tendencias)
                print("Relatório em PDF gerado com sucesso (relatorio.pdf).")
        else:
            print("Opção inválida. Tente novamente.")
