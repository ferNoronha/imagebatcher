import typer
import yaml

from pathlib import Path
from imagebatcher.pipeline import run_pipeline

app = typer.Typer()

@app.command()
def process(
    input: str = typer.Argument(..., help="Input file path"), 
    output: str = typer.Argument(..., help="Output file path"), 
    steps: str = typer.Option("resize,normalize", help="Comma-separated list of processing steps"), 
    workers: int = typer.Option(4, help="Number of worker threads to use for processing"),
    verbose: bool = typer.Option(True, help="Enable verbose logging")):
    
    typer.echo(f"Processing images from {input} to {output} with steps: {steps}")
    
    input_path = Path(input)
    output_path = Path(output)
    step_list = [s.strip() for s in steps.split(",")]
    run_pipeline(
        input_path=input_path, 
        output_path=output_path, 
        step_list=step_list,
        max_workers=workers, 
        verbose=verbose)

@app.command()
def run_config(config: str = typer.Option("pipeline.yaml", help="Path to the pipeline configuration file (YAML)")):
    """Executa pipeline com base em um arquivo pipeline.yaml"""
    with open(config, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    input_path = Path(data["input"])
    output_path = Path(data["output"])
    steps = data["steps"]
    workers = data.get("workers", 4)
    verbose = data.get("verbose", True)
    step_params = data.get("steps_params", {})

    run_pipeline(
        input_path=input_path,
        output_path=output_path,
        step_list=steps,
        max_workers=workers,
        verbose=verbose,
        step_params=step_params
    )
    
if __name__ == "__main__":
    app()