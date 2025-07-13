from PIL import ImageFilter

def process(image, radius=2, **kwargs):
    try:
        if radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        return image.filter(ImageFilter.GaussianBlur(radius=radius))
    except Exception as e:
        logger = kwargs.get('logger')
        if logger:
            logger.error(f"[ERROR] Erro ao aplicar desfoque: {str(e)}")
        raise ValueError(f"[ERROR] Erro ao aplicar desfoque: {str(e)}")