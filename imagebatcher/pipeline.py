from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from PIL import Image
from time import perf_counter
from .steps import available_steps
from .logger import setup_logger

import os
import json

def process_single_image(filename, input_path, output_path, step_list, logger=None, verbose=True, step_params=None):
    report = {
            "filename": filename,
            "steps": [],
            "durations": {},
            "status": "ok",
            "error": None
        }
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
                try: 
                    step_args = step_params.get(step, {}) if step_params else {}
                    if verbose and logger:
                        logger.info(f"[INFO] >> Aplicando step: {step} ({filename}) {step_args}")
                    
                    start_time = perf_counter()
                    image = available_steps[step](
                        image,
                        filename=filename,
                        output_path=output_path,
                        logger=logger if verbose else None,
                        **step_args
                    )
                    end_time = perf_counter()
                    duration = round(end_time - start_time, 4)
                    report["steps"].append(step)
                    report["durations"][step] = duration

                except Exception as e:
                    report["status"] = "error"
                    report["error"] = f"[{step}] {str(e)}"
                    if verbose and logger:
                        logger.error(f"[ERROR] Erro ao aplicar step '{step}' em {filename}: {str(e)}")
                    break
            else:
                if verbose and logger:
                    logger.warning(f"[WARNING] Step '{step}' não encontrado.")

        if report["status"] == "ok":
            image.save(output_path / "images" / filename)
            if verbose and logger:
                logger.info(f"[OK] Finalizado: {filename}")

    except Exception as e:
        report["status"] = "error"
        report["error"] = f"[load] {str(e)}"
        if verbose and logger:
            logger.error(f"[ERROR] Erro ao processar {filename}: {str(e)}")

    return report

def run_pipeline(input_path, output_path, step_list: list[str], max_workers: int = 4, verbose: bool = True, report_verbose: bool = False, step_params=None):
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "images").mkdir(exist_ok=True)
    (output_path / "texts").mkdir(exist_ok=True)

   
    logger = setup_logger(output_path) if verbose else None
    if verbose and logger:
        logger.info(f"[INFO] Iniciando processamento. Steps: {step_list}")

    report_path = output_path / "report.json"

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

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processando imagens"):
            report = future.result()
            if report_verbose:
                with open(report_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(report, ensure_ascii=False) + "\n")
    
    if verbose and logger:
        logger.info("[FINISHED] Pipeline finalizado.")

