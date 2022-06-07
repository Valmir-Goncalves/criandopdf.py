arquivo = 'Curso De PDF.pdf'
titulo = 'integrando python com pdf'
titulo_conteudo = 'Valmir apresenta'
subtitulo_conteudo = 'aprenda a manipular arquivos PDF com python'

conteudo_curso = [
    'neste curso voce aprendera',
    'extrair texto de pdf existente',
    'juntar pdfs',
    'adicionar senhas',
    'criar um pdf do zero'
]
logo_azumy = 'pg.png'

from reportlab.lib.pagesizes import A4 #  (210*mm,297*mm)
from reportlab.lib.units import cm, inch, mm
from reportlab.pdfgen import canvas

pdf = canvas.Canvas(arquivo, pagesize=A4)
pdf.setTitle(titulo_conteudo)


# Conversor de tamanhos

def mostrar_tamanho():
    print(f'1 mm vale {mm} pontos')
    print(f'1 cm vale {cm} pontos')
    print(f'1 polegada vale {inch} pontos')
mostrar_tamanho()

# Desenhar regua
def desenhar_regua(pdf, pagina):
    pdf.setFontSize('8') # almenta o tamanho da regua
    pagina_y = int(pagina[1] / cm)
    pagina_x = int(pagina[0] / cm)

    for y in range(pagina_y):
        pdf.drawString(0 * cm, y * cm, f'y{y}')

    for x in range(pagina_x):
        pdf.drawString(x * cm, 29 * cm, f'x{x}')


desenhar_regua(pdf, A4)

# configurar fonte
# ver fontes disponiveis
# print(pdf.getAvaiableFonts())

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(
    TTFont('OpenSans', 'OpenSans-Regular.ttf')
)
pdf.setFont('OpenSans', 36)
# Almenta o tamanho da fonte

pdf.drawString(7 * cm, (29.7 - 3) * cm, titulo_conteudo)
pdf.setFontSize(20) # ALMENTA O TAMANHO DO TEXTO
pdf.drawString(2 * cm, (29.7 - 5) * cm, arquivo)
pdf.drawString(2 * cm, (29.7 - 6) * cm, subtitulo_conteudo)

# salvando arquivo
pdf.save()
