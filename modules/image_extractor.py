import pytesseract
from PIL import Image
import io

def extract_text_from_image(file):

    image = Image.open(io.BytesIO(file.read()))

    text = pytesseract.image_to_string(image)

    return text