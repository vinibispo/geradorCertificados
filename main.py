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
    nome_arquivo = "pessoas.xlsx"
    planilha_nomes = open_workbook(nome_arquivo)
    folha_planilha = planilha_nomes.sheet_by_index(0)
    for i in range(1, folha_planilha.nrows):
        pessoa_nome = folha_planilha.row_values(i)[0]
        gera_certificado(pessoa_nome)
pega_dado_excel()