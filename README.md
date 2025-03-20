# Chicken Disease Classification

## Project Overview
This project implements a deep learning system for classifying chicken diseases from images. It provides a robust framework for identifying various chicken diseases, helping in early detection and treatment.

## Project Workflow
1. Data Ingestion - Downloading and extracting the dataset
2. [Future stages to be implemented]

## Technologies Used
- **Deep Learning Framework**: TensorFlow/Keras or PyTorch
- **Containerization**: Docker
- **Continuous Integration/Continuous Deployment**: GitHub Actions or Jenkins
- **Cloud Services**: AWS and Azure for deployment
- **Data Version Control**: DVC for managing datasets and model versions

## Installation

### Prerequisites
- Python 3.x
- pip

### Setup
1. Clone the repository
```bash
git clone https://github.com/ArihantSingla21/Chicken-Disease-Classification.git
cd Chicken-Disease-Classification
```

2. Install dependencies
```bash
pip install -e .
```

## Project Structure
```
Chicken-Disease-Classification/
├── config/
│ └── config.yaml # Main configuration settings
├── src/
│ └── chicken_disease_classification/
│ ├── components/ # Modular components
│ │ └── data_ingestion.py
│ ├── config/ # Configuration handling
│ │ └── configuration.py
│ ├── constants/ # Project constants
│ ├── entity/ # Data classes and entities
│ │ └── config_entity.py
│ ├── pipeline/ # Processing pipelines
│ │ └── stage_01_data_ingestion.py
│ └── utils/ # Utility functions
│ └── common.py
├── research/ # Experimental notebooks
│ ├── 01_data_ingestion.ipynb
│ └── trials.ipynb
├── main.py # Entry point for the application
├── params.yaml # Model parameters
└── setup.py # Package setup
```


## Execution
The project can be run using the main.py file:

```bash
python main.py
```

This will execute the data ingestion pipeline that downloads and extracts the chicken disease image dataset.

## Configuration
The project uses YAML configuration files:
- `config/config.yaml`: Contains paths and URLs for data ingestion
- `params.yaml`: Contains model parameters

## Components

### Data Ingestion
The data ingestion component downloads chicken disease images and extracts them for further processing and model training.

### Configuration
Configuration management provides a clean separation of code and configuration, allowing for easy modification of parameters without changing code.

## Features
- Image classification for chicken diseases
- Modular pipeline architecture
- Configuration-driven execution
- Utility functions for:
  - YAML configuration management
  - JSON data handling
  - Binary file operations
  - Image encoding/decoding in base64
  - Directory management
  - File size tracking

## Usage
The project includes various utility functions that can be imported from the package:

```python
from chicken_disease_classification.utils.common import (
    read_yaml,
    create_directories,
    save_json,
    load_json,
    save_bin,
    load_bin,
    get_size,
    encodeImageIntoBase64,
    decodeImage
)
```

## Author
- Name: Arihant Singla
- Email: arihantsingla21@gmail.com
- GitHub: [@ArihantSingla21](https://github.com/ArihantSingla21)

## License
This project is licensed under standard open-source terms.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Issues
For any issues or feature requests, please use the [GitHub Issue Tracker](https://github.com/ArihantSingla21/Chicken-Disease-Classification/issues).