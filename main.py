from PIL import Image, ImageFont, ImageDraw
from xlrd import open_workbook
def gera_certificado(nome_completo_pessoa):
    certificado = 'certificado'
    certificado_pessoa = certificado +nome_completo_pessoa.replace(" ", "").lower()+ ".png"
    certificado += ".png"
    imagem_certificado = Image.open(certificado)
    imagem_certificado_desenho = ImageDraw.Draw(imagem_certificado)
    caminho_imagem = "fonts/SourceSerifPro-Bold.ttf"
    fonte_certificado = ImageFont.truetype(caminho_imagem, 44, encoding="unic")
    text_size = imagem_certificado_desenho.textsize(nome_completo_pessoa, fonte_certificado)

    imagem_certificado_desenho.text(((imagem_certificado.size[0] - text_size[0])/ 2, 243), nome_completo_pessoa.upper(), font=fonte_certificado, fill=(115,111,72))
    imagem_certificado.save("images/" +certificado_pessoa, "PNG", resolution=100.0)
    return certificado_pessoa
def pega_dado_excel():
    planilha_nomes = open_workbook