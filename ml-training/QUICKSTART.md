# Quick Start - 5 Minutes to Trained Model

## Prerequisites
- Python 3.9 or 3.10
- macOS (for Core ML conversion)

## Steps

### 1. Setup (First Time Only)
```bash
cd ml-training

# Mac/Linux:
chmod +x setup.sh
./setup.sh

# Windows:
setup.bat
```

### 2. Activate Environment
```bash
# Mac/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Test Setup (Optional but Recommended)
```bash
python test_setup.py
```

Expected output:
```
✅ PASS - Python Version
✅ PASS - Package Imports
✅ PASS - Training Data
✅ PASS - Model Architecture
```

### 4. Train Model (~5 minutes)
```bash
python train_model.py
```

Expected output:
```
Epoch 100/100: Loss = 0.1234, Accuracy = 95.00%
✅ Model saved to models/compliment_scorer.pth
```

### 5. Convert to Core ML (~2 minutes)
```bash
python convert_to_coreml.py
```

Expected output:
```
✅ Core ML model saved!
📊 Model size: 6.32 MB
```

### 6. Files Created
```
models/
├── ComplimentScorer.mlpackage/  ← Add this to iOS
├── vocabulary.txt               ← Add this to iOS
├── compliment_scorer.pth        ← PyTorch backup
└── tokenizer.pkl                ← Tokenizer backup
```

## Next: iOS Integration

See `GUIDE.md` Part 2 for iOS integration steps.

## Troubleshooting

**"command not found: python"**
- Try `python3` instead of `python`

**"No module named 'torch'"**
- Make sure virtual environment is activated
- Run: `pip install -r requirements.txt`

**"coremltools not found"**
- Only works on macOS
- Install: `pip install coremltools`

**Training accuracy stuck at 30%**
- Let it run all 100 epochs
- Should improve steadily
- Final accuracy should be 90%+

## That's It!

You now have a trained ML model ready for iOS.

Next step: Copy `ComplimentScorer.mlpackage` to your iOS project.
