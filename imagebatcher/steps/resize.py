def process(image, width = 800, height = 0, **kwargs):
    if not width:
        return image
    try:
        if height == 0:
            height = int(width * (image.size[1] / image.size[0]))
        return image.resize((width, height))
    except (ValueError, IndexError):
        logger = kwargs.get('logger')
        if logger:
            logger.error(f"Erro ao processar resize_shape: '{width,height}'. Use 'largura,altura' ou apenas 'largura'.")
        raise ValueError(f"resize_shape inválido: '{width,height}'. Use 'largura,altura' ou apenas 'largura'.")
    