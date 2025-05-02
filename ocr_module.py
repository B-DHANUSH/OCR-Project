import pytesseract
import cv2
import numpy as np
from PIL import Image

def image_to_text(image: Image.Image) -> str:
    try:
        open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        return pytesseract.image_to_string(gray)
    except:
        return ""
