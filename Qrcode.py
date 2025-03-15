import qrcode
from PIL import Image  # Import the Image module from the PIL library

# --- Code from the original file ---
data = 'https://www.linkedin.com/in/jessica-ap-bueno/'

img = qrcode.make(data)

type(img)  # qrcode.image.pil.PilImage

img.save('C:/Users/bueno/OneDrive/Área de Trabalho/Aprendendo Python Files/new/qrcode.png')
