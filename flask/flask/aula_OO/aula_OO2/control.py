#from model import vcard
import qrcode

def qrcode_gen(nome):
    image = qrcode.make(nome)
    image.save("./static/qrcode.jpeg")
    

