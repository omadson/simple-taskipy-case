import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from kaggle.api.kaggle_api_extended import KaggleApi

dataset = "zynicide/wine-reviews"
target_dir = Path("data/raw")
target_dir.mkdir(parents=True, exist_ok=True)


api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    dataset,
    path=target_dir,
    unzip=True
)

print(f"Dataset '{dataset}' baixado em {target_dir}")