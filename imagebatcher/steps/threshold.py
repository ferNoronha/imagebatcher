def process(image, threshold=128, **kwargs):
    try:
        if not (0 <= threshold <= 255):
            raise ValueError("Threshold must be between 0 and 255.")
        image = image.convert("L")
        return image.point(lambda p: 255 if p > threshold else 0)
    except Exception as e:
        logger = kwargs.get('logger')
        if logger:
            logger.error(f"[ERROR] Erro ao aplicar threshold: {str(e)}")
        raise ValueError(f"[ERROR] Erro ao aplicar threshold: {str(e)}")