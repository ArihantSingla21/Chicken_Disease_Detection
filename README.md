# 🔬 Chicken Disease Classification Project

## 📌 Overview
An end-to-end deep learning project that uses computer vision to classify chicken diseases from images. This project implements a robust CNN architecture to help farmers and veterinarians quickly identify common chicken diseases, enabling faster treatment and better flock management.

## 🎯 Features
- Real-time disease classification
- Modern web interface with drag-and-drop functionality
- High-accuracy prediction model
- Confidence score for predictions
- Support for multiple image formats
- Responsive design for all devices

## 🛠️ Tech Stack
### ML Stack
- TensorFlow/Keras for deep learning
- CNN Architecture for image classification
- Python for backend processing
- NumPy for numerical computations
- OpenCV for image processing

### Web Stack
- Flask for backend server
- HTML/CSS/JavaScript for frontend
- Bootstrap for responsive design
- jQuery for AJAX requests
- Font Awesome for icons

### DevOps
- Docker for containerization
- DVC for data version control
- GitHub Actions for CI/CD
- AWS/Azure for cloud deployment

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. Clone the repository
```bash
git clone https://github.com/ArihantSingla21/Chicken-Disease-Classification.git
cd Chicken-Disease-Classification
```
Chicken-Disease-Classification/
├── config/
│ └── config.yaml # Configuration settings
├── src/
│ └── chicken_disease_classification/
│ ├── components/ # Core components
│ │ └── data_ingestion.py
│ ├── config/ # Configuration handling
│ │ └── configuration.py
│ ├── constants/ # Project constants
│ ├── entity/ # Data classes
│ │ └── config_entity.py
│ ├── pipeline/ # Processing pipelines
│ │ └── stage_01_data_ingestion.py
│ └── utils/ # Utility functions
│ └── common.py
├── templates/ # HTML templates
│ └── index.html # Main web interface
├── static/ # Static files
├── research/ # Research notebooks
│ ├── trials.ipynb
│ └── experiments.ipynb
├── app.py # Flask application
├── main.py # Entry point
├── params.yaml # Model parameters
├── requirements.txt # Dependencies
└── setup.py # Package setup

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

The application will be available at `http://localhost:8080`

## 🔄 Project Workflow

1. **Data Ingestion**
   - Download and extract dataset
   - Split into train/test sets
   - Validate data integrity

2. **Data Preprocessing**
   - Image resizing and normalization
   - Data augmentation
   - Format standardization

3. **Model Development**
   - CNN architecture design
   - Model training and validation
   - Hyperparameter tuning

4. **Deployment**
   - Flask web application
   - API development
   - Docker containerization

## 📊 Model Performance

- Training Accuracy: ~95%
- Validation Accuracy: ~93%
- Test Accuracy: ~92%

Supported Disease Classifications:
- Coccidiosis
- Salmonella
- New Castle Disease
- Healthy Chicken

## 💻 Usage

1. Access the web interface
2. Upload a chicken image through drag-drop or file selection
3. Click "Analyze" to get disease prediction
4. View results with confidence scores

## 🛡️ Configuration

The project uses YAML configuration files:
- `config/config.yaml`: Main configuration
- `params.yaml`: Model parameters

Example configuration:
```yaml
artifacts_root: artifacts
data_ingestion:
  root_dir: artifacts/data_ingestion
  source_URL: <dataset_url>
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
- **Arihant Singla**
  - Email: arihantsingla21@gmail.com
  - GitHub: [@ArihantSingla21](https://github.com/ArihantSingla21)

## 🙏 Acknowledgments
- Dataset providers
- Open source community
- Research papers and references

## 📞 Support
For support, email arihantsingla21@gmail.com or open an issue in the repository.

## 🔗 Links
- [Project Demo](https://your-demo-link)
- [Documentation](https://your-docs-link)
- [Dataset Source](https://your-dataset-link)