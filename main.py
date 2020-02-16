from PIL import Image, ImageFont, ImageDraw
def gera_certificado(nome_pessoa):
    certificado = 'certificado.png'
    imagem_certificado = Image.open(certificado)
    imagem_certificado_desenho = ImageDraw.Draw(imagem_certificado)
    caminho_imagem = "./fonts/SourceSerifPro-Bold.ttf"
    fonte_certificado = ImageFont.truetype(caminho_imagem)
    imagem_certificado_desenho.text((640, 1000), nome_pessoa, font=fonte_certificado, fill=(115,111,72))
# gera_certificado()