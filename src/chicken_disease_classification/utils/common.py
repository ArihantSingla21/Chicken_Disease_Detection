import os 
import box.exceptions
import yaml
import json
import joblib
import numpy as np
import pandas as pd
from tqdm import tqdm
from src.chicken_disease_classification import logger
from typing import Dict, Any, Optional, Union, List
import base64
import dill 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path

# The @ensure_annotations decorator is used to enforce type annotations in function parameters and return values.
# It checks that the types of the arguments passed to the function and the return type match the specified annotations.
# This can help catch type-related errors early in the development process.
@ensure_annotations
def read_yaml(file_path: Union[str, Path]) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox.

    Args:
        file_path (Union[str, Path]): The path to the YAML file to be read.

    Returns:
        ConfigBox: A ConfigBox containing the contents of the YAML file.

    Logs:
        - Information about the file being read.
        - Confirmation of successful reading of the file.
        - Error message if the file cannot be read.
    """
    logger.info(f"Reading YAML file from: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = yaml.safe_load(file)  # Safely load the YAML content
            logger.info("YAML file read successfully.")
            return ConfigBox(content) # this helps in proper output of the yaml file in json format , accessing becomes more intuitive and easy
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e

@ensure_annotations
def save_json(path: Union[str, Path], data: dict):
    """
    Save json data
    
    Args:
        path (Union[str, Path]): path to json file
        data (dict): data to be saved in json file
    """
    path = Path(path) if isinstance(path, str) else path
    with open(path, "w") as f:
        json.dump(data, f, indent=4)



## for loss and accuracy matrix , as an example to be saved in the logs folder
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def load_json(path: Union[str, Path]) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox.

    Args:
        path (Union[str, Path]): The path to the JSON file to be loaded.
    """
    with open(path, 'r', encoding='utf-8') as file:
        content = json.load(file)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def get_size(file_path: Union[str, Path]) -> int:
    """
    Returns the size of the specified file in bytes.

    Args:
        file_path (Union[str, Path]): The path to the file whose size is to be determined.

    Returns:
        int: The size of the file in bytes.
    """
    size = os.path.getsize(file_path)
    logger.info(f"Size of the file at {file_path}: {size} bytes")
    return size


@ensure_annotations
def save_bin(data: Any, path: Union[str, Path]) -> None:
    """
    Saves data to a binary file.

    Args:
        data (Any): The data to be saved.
        path (Union[str, Path]): The path to the binary file to be saved.

    Logs:
        - Information about the file being saved.
        - Confirmation of successful saving of the file.
    """
    joblib.dump(value= data, filename= path)
    logger.info(f"Binary file saved successfully at: {path}")
    

@ensure_annotations
def load_bin(path: Union[str, Path]) -> Any:
    """
    Loads data from a binary file.

    Args:
        path (Union[str, Path]): The path to the binary file to be loaded.

    Returns:
        Any: The data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data




@ensure_annotations
def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
    f.close()

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read())













