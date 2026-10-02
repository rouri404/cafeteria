from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle  
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

def adicionar_rodape(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.HexColor('#64748B')) # Cor cinza para o texto
    
    # Texto do rodapé
    texto_esquerda = "Responsável: Gabriel Couto"
    texto_direita = f"Página {doc.page}"
    
    canvas.drawRightString(572, 25, texto_direita)

    canvas.setStrokeColor(colors.HexColor('#CBD5E1'))
    canvas.setLineWidth(0.5)
    canvas.line(40, 40, 572, 40)
    
    canvas.restoreState()

def gerar_pdf(filename="relatorio.pdf"): 
    # Configurações do documento PDF (Aumentei a margem inferior para 50 para o texto não sobrepor o rodapé)
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=50)  
    styles = getSampleStyleSheet()
    story = []
    
    # Conteúdo do relatório
    styles['Heading1'].alignment = TA_CENTER

    story.append(Paragraph("Cafeteria", styles['Heading1']))  
    story.append(Paragraph("<b>Relatório de Estoque:</b> 02/10/2026", styles['Heading2']))
    story.append(Spacer(1, 15))

    dados = [
        ["ID", "Nome", "Valor"],
        ["001", "Café em Grão Blend (kg)", "120.00"], 
        ["002", "Café em Grão Especial (kg)", "180.00"],
        ["003", "Leite Integral B-Box (L)", "45.00"],
        ["004", "Bebida Vegetal Aveia (L)", "65.00"],
        ["005", "Xarope de Baunilha (Un)", "85.00"],
        ["006", "Açúcar Sachê (Cx 1000un)", "35.00"],
        ["007", "Croissant Congelado (Pct)", "150.00"],
        ["008", "Pão de Queijo Mineiro (kg)", "40.00"],
        ["009", "Brownie de Chocolate (Un)", "90.00"],
        ["010", "Água Mineral s/ Gás (Fardo)", "24.00"],
        ["011", "Suco Integral Laranja (Un)", "55.00"],
        ["012", "Copo Papel 240ml (Cx 500un)", "110.00"],
        ["013", "Tampa Copo 240ml (Cx 500un)", "45.00"],
        ["014", "Mexedor de Madeira (Pct)", "15.00"],
        ["015", "Guardanapo Sachê (Cx)", "30.00"],
        ["016", "Detergente Máquina Espresso (Un)", "95.00"],
        ["017", "Filtro de Papel V60 (Pct)", "38.00"]
    ]
    
    # Ajustei as larguras para somarem 532 (largura útil da página)
    tabela = Table(dados, colWidths=[80, 332, 120])  
    tabela.setStyle(TableStyle([  
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#6f4e37")), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), 
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),  
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])  
    ]))

    story.append(tabela)  
    story.append(Spacer(1, 20))
    story.append(Paragraph("Nota: Este relatório reflete o nível de suprimentos atual e deve ser atualizado semanalmente.", styles['Normal']))

    # --- ALTERAÇÃO AQUI: Passando a função para o build ---
    doc.build(story, onFirstPage=adicionar_rodape, onLaterPages=adicionar_rodape) 
    print(f"PDF gerado com sucesso: {filename}")  

if __name__ == "__main__": 
    gerar_pdf()
