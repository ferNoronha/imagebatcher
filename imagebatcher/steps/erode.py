import numpy as np
import cv2
from PIL import Image

def process(image, kernel_size=3, iterations=1, **kwargs):
    try:
        if kernel_size <= 0 or iterations < 1:
            raise ValueError("Kernel size must be a positive integer and iterations must be at least 1.")
        image_gray = image.convert("L")
        img_np = np.array(image_gray)

        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        eroded = cv2.erode(img_np, kernel, iterations=iterations)

        return Image.fromarray(eroded)
    except Exception as e:
        logger = kwargs.get('logger')
        if logger:
            logger.error(f"[ERROR] Erro ao aplicar erosão: {str(e)}")
        raise ValueError(f"[ERROR] Erro ao aplicar erosão: {str(e)}")
    