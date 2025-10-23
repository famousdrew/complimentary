# Complimentary ML Training

This directory contains everything needed to train and convert the ML model for the Complimentary app.

## Setup Instructions

### 1. Install Python
You need Python 3.9 or 3.10 (3.11+ may have compatibility issues with some packages).

**Check your Python version:**
```bash
python --version
```

If you don't have Python installed:
- **macOS:** Download from [python.org](https://www.python.org/downloads/) or use `brew install python@3.10`
- **Windows:** Download from [python.org](https://www.python.org/downloads/)

### 2. Create Virtual Environment
```bash
# Navigate to this directory
cd ml-training

# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model
```bash
python train_model.py
```

This will:
- Load the training data
- Train the compliment scorer model
- Convert it to Core ML format
- Save `ComplimentScorer.mlpackage` in the `models/` directory

### 5. Use the Model
The generated `ComplimentScorer.mlpackage` file will be copied to your iOS project.

## Files

- `requirements.txt` - Python dependencies
- `train_model.py` - Training script
- `training_data.py` - Training dataset
- `model.py` - Model architecture
- `convert_to_coreml.py` - Conversion script
- `models/` - Output directory for trained models

## Model Details

**Type:** LSTM-based text classifier
**Size:** ~5-10MB
**Input:** Text string (up to 200 characters)
**Output:**
- Score (1-5 stars)
- Confidence (0-1)
- Specificity metrics

## Training Data

The model is trained on ~200 hand-labeled compliment examples spanning:
- Generic compliments (1-2 stars)
- Moderate compliments (3 stars)
- Specific compliments (4-5 stars)

You can add more training data in `training_data.py`.
