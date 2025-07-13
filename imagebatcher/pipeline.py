from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from PIL import Image
import os
from .steps import available_steps
from .logger import setup_logger

def process_single_image(filename, input_path, output_path, step_list, logger=None, verbose=True, step_params=None):
    try:
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            if verbose and logger:
                logger.warning(f"[WARNING] Ignorando arquivo não suportado: {filename}")
            return

        if verbose and logger:
            logger.info(f"[INFO] Processando {filename}")
        image_path = input_path / filename
        image = Image.open(image_path)

        for step in step_list:
            if step in available_steps:
                if verbose and logger:
                    logger.info(f"[INFO] >> Aplicando step: {step} ({filename})")
                step_args = step_params.get(step, {}) if step_params else {}
                image = available_steps[step](
                    image,
                    filename=filename,
                    output_path=output_path,
                    logger=logger,
                    **step_args
                )
            else:
                if verbose and logger:
                    logger.warning(f"[WARNING] Step '{step}' não encontrado.")

        image.save(output_path / "images" / filename)
        if verbose and logger:
            logger.info(f"[OK] Finalizado: {filename}")
    except Exception as e:
        if logger:
            logger.error(f"[ERROR] Erro ao processar {filename}: {str(e)}")


def run_pipeline(input_path, output_path, step_list: list[str], max_workers: int = 4, verbose: bool = True, step_params=None):
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "images").mkdir(exist_ok=True)
    (output_path / "texts").mkdir(exist_ok=True)

   
    logger = setup_logger(output_path) if verbose else None
    if verbose and logger:
        logger.info(f"[INFO] Iniciando processamento. Steps: {step_list}")

    image_files = [f for f in os.listdir(input_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                process_single_image,
                filename,
                input_path,
                output_path,
                step_list,
                logger,
                verbose,
                step_params
            ): filename for filename in image_files
        }

        for _ in tqdm(as_completed(futures), total=len(futures), desc="Processando imagens"):
            pass

    if verbose and logger:
        logger.info("[FINISHED] Pipeline finalizado.")

