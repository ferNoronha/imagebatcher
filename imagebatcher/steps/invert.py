from PIL import ImageOps
def process(image, **kwargs):
    try:
        return ImageOps.invert(image.convert("RGB"))
    except Exception as e:
        logger = kwargs.get('logger')
        if logger:  
            logger.error(f"[ERROR] Erro ao inverter cores imagem: {str(e)}")
        raise ValueError(f"[ERROR] Erro ao inverter cores imagem: {str(e)}")