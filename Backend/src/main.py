import os
from src.pipeline.main import run_pipeline

if __name__ == "__main__":
    sample_file = os.path.join("src", "data", "bills.csv")
    run_pipeline(sample_file)
