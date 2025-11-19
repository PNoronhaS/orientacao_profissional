import json
from fpdf import FPDF
from .modelos import Perfil

def salvar_perfil(perfil: Perfil, caminho="perfil.json"):
    """Salva perfil em arquivo JSON."""
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump({"nome": perfil.nome, "competencias": perfil.competencias}, f, indent=4)

def carregar_perfil(caminho="perfil.json"):
    """Carrega perfil de arquivo JSON, se existir."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return Perfil(dados["nome"], dados["competencias"])
    except FileNotFoundError:
        return None

def gerar_relatorio_pdf(perfil, recomendacoes, tendencias, caminho="relatorio.pdf"):
    """Gera relatório em PDF com perfil, recomendações e tendências."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Relatório de Orientação Profissional", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, f"Nome: {perfil.nome}", ln=True)
    pdf.cell(200, 10, "Competências:", ln=True)
    for comp, nivel in perfil.competencias.items():
        pdf.cell(200, 10, f"- {comp}: nível {nivel}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, "Recomendações de Carreira:", ln=True)
    for carreira, compat in recomendacoes:
        pdf.cell(200, 10, f"- {carreira.nome} ({int(compat*100)}%)", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, "Tendências Futuras:", ln=True)
    for t in tendencias:
        pdf.cell(200, 10, f"- {t}", ln=True)

    pdf.output(caminho)
