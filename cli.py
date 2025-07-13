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
    verbose: bool = typer.Option(True, help="Enable verbose logging"),
    report: bool = typer.Option(False, help="Generate a report of the processing steps"),
    step_params: str = typer.Option("", help="Optional parameters for each step in the format 'step_name:param1=value1,param2=value2'")):
    
    input_path = Path(input)
    output_path = Path(output)
    step_list = [s.strip() for s in steps.split(",")]
    run_pipeline(
        input_path=input_path, 
        output_path=output_path, 
        step_list=step_list,
        max_workers=workers, 
        verbose=verbose,
        report_verbose=report,
        step_params=step_params)

@app.command()
def run_config(config: str = typer.Option("pipeline.yaml", help="Path to the pipeline configuration file (YAML)")):
    
    with open(config, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    input_path = Path(data["input"])
    output_path = Path(data["output"])
    steps = data["steps"]
    workers = data.get("workers", 4)
    verbose = data.get("verbose", True)
    report = data.get("report", False)
    step_params = data.get("steps_params", {})

    run_pipeline(
        input_path=input_path,
        output_path=output_path,
        step_list=steps,
        max_workers=workers,
        verbose=verbose,
        report_verbose=report,
        step_params=step_params
    )
    
if __name__ == "__main__":
    app()