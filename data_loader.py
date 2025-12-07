# data_loader.py
import kagglehub
import os

def download_dataset(dataset_id: str, download_path: str = "data/") -> str:
    """
    Download dataset from KaggleHub.
    
    Args:
        dataset_id (str): KaggleHub dataset ID
        download_path (str): Local path for dataset
    
    Returns:
        str: Path where dataset is downloaded
    """
    os.makedirs(download_path, exist_ok=True)
    path = kagglehub.dataset_download(dataset_id, path=download_path)
    return path
