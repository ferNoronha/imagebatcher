from PIL import ImageOps

def process(image, cutoff=0, **kwargs):
    try:
        if not (0 <= cutoff <= 100):
            raise ValueError("Cutoff must be between 0 and 100.")
        return ImageOps.autocontrast(image, cutoff=cutoff)
    except Exception as e:
        logger = kwargs.get('logger')
        if logger:
            logger.error(f"[ERROR] Erro ao aplicar autocontrast: {str(e)}")
        raise ValueError(f"[ERROR] Erro ao processar imagem: {str(e)}")