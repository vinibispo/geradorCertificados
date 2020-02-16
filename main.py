from PIL import Image, ImageFont, ImageDraw
def gera_certificado(nome_pessoa):
    certificado = 'certificado'
    certificado_pessoa = certificado + nome_pessoa + ".png"
    certificado += ".png"
    imagem_certificado = Image.open(certificado)
    imagem_certificado_desenho = ImageDraw.Draw(imagem_certificado)
    caminho_imagem = "fonts/SourceSerifPro-Bold.ttf"
    fonte_certificado = ImageFont.truetype(caminho_imagem, 44, encoding="unic")
    imagem_certificado_desenho.text((34, 243), nome_pessoa.upper().center(20), font=fonte_certificado, fill=(115,111,72))
    imagem_certificado.save("images/" +certificado_pessoa, "PNG", resolution=100.0)
    return certificado_pessoa
print(gera_certificado("Adolfo"))