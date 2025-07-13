def process(image, **kwargs):
    try:
        return image.convert("L")
    except Exception as e:
        logger = kwargs.get('logger')
        if logger:
            logger.error(f"[ERROR] Erro ao converter imagem para escala de cinza: {str(e)}")
        raise ValueError(f"[ERROR] Erro ao processar imagem: {str(e)}")