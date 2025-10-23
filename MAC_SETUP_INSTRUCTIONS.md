# Mac Setup Instructions - Continue ML Training

## 🎯 What We've Done So Far

✅ Created complete ML training pipeline
✅ Built React Native app with rule-based analysis
✅ Created 100+ labeled training examples
✅ Set up all Python scripts and documentation
✅ Committed everything to GitHub

## 📍 Where You Left Off

You're ready to **train the ML model** on your Mac, which is required for Core ML conversion.

---

## 🚀 Quick Start on Mac

### Step 1: Clone the Repository

```bash
# Open Terminal on Mac
cd ~/Desktop  # or wherever you want the project

git clone https://github.com/famousdrew/complimentary.git
cd complimentary
```

### Step 2: Navigate to ML Training

```bash
cd ml-training
```

### Step 3: Setup Python Environment

```bash
# Run setup script
chmod +x setup.sh
./setup.sh

# Activate virtual environment
source venv/bin/activate
```

**Expected output:**
```
Step 1: Creating virtual environment...
Step 2: Activating virtual environment...
Step 3: Installing dependencies...
✅ Setup Complete!
```

### Step 4: Test Setup (Optional but Recommended)

```bash
python test_setup.py
```

**Expected output:**
```
✅ PASS - Python Version
✅ PASS - Package Imports
✅ PASS - Training Data
✅ PASS - Model Architecture
✅ PASS - Core ML Tools
```

### Step 5: Train the Model (~5 minutes)

```bash
python train_model.py
```

**What happens:**
- Trains LSTM model on 100 examples
- Takes ~5 minutes
- Shows progress bars for each epoch
- Final accuracy should be 90%+

**Expected output:**
```
Epoch 1/100: Loss = 1.4523, Accuracy = 32.00%
Epoch 2/100: Loss = 1.2145, Accuracy = 48.00%
...
Epoch 100/100: Loss = 0.1234, Accuracy = 95.00%

✅ Model saved to models/compliment_scorer.pth
```

### Step 6: Convert to Core ML (~2 minutes)

```bash
python convert_to_coreml.py
```

**Expected output:**
```
✅ Model loaded successfully
✅ Conversion successful!
📊 Model size: 6.32 MB

📦 Core ML model: models/ComplimentScorer.mlpackage
📄 Vocabulary file: models/vocabulary.txt
```

### Step 7: Verify Files Created

```bash
ls -lh models/
```

**You should see:**
```
ComplimentScorer.mlpackage/  ← This is what you need for iOS!
vocabulary.txt               ← Also needed for iOS
compliment_scorer.pth        ← PyTorch backup
tokenizer.pkl                ← Tokenizer backup
```

---

## 🎉 Success! What's Next?

Once training is complete, you'll have:
- ✅ `ComplimentScorer.mlpackage` - Ready for iOS
- ✅ `vocabulary.txt` - Word mappings for iOS

### Next Steps in This Session:

1. **Add model to iOS project** (I'll help with this)
2. **Create Swift bridge module** (I'll write the code)
3. **Test the integration**

---

## 🐛 Troubleshooting

### "python: command not found"

Try `python3` instead:
```bash
python3 train_model.py
```

### "No module named 'torch'"

Make sure virtual environment is activated:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### "coremltools not found"

This should install automatically, but if not:
```bash
pip install coremltools
```

### Training accuracy stuck low

- Let it run all 100 epochs
- Should improve steadily
- If stuck at <70% after 100 epochs, something's wrong (ask me!)

### Permission denied on setup.sh

```bash
chmod +x setup.sh
./setup.sh
```

---

## 📚 Reference Documents

Once you're on Mac, refer to:

1. **Quick commands:** `ml-training/QUICKSTART.md`
2. **Detailed guide:** `ml-training/GUIDE.md`
3. **Overview:** `ML_INTEGRATION_SUMMARY.md`

---

## ⏱️ Time Estimate

- Setup: 5 minutes
- Training: 5 minutes
- Conversion: 2 minutes
- **Total: ~12 minutes**

---

## 💡 Tips

1. **Use Terminal** (not iTerm if you want to avoid issues)
2. **Make sure you have internet** for pip installs
3. **Don't close Terminal** until training is complete
4. **Commit the trained model** after conversion (optional)

---

## 🆘 If Something Goes Wrong

Just open a new Claude Code session on your Mac and say:

> "I cloned the complimentary repo and I'm ready to train the ML model. I'm at the ml-training directory."

I'll pick up from there!

---

## 📦 What Gets Created

After successful training:

```
ml-training/
├── venv/                              ← Virtual environment (auto-created)
└── models/                            ← Created after training
    ├── ComplimentScorer.mlpackage/    ← For iOS (6-10MB)
    ├── vocabulary.txt                 ← For iOS (50KB)
    ├── compliment_scorer.pth          ← PyTorch model (backup)
    └── tokenizer.pkl                  ← Tokenizer (backup)
```

---

## ✅ Checklist

On your Mac:

- [ ] Clone repo: `git clone https://github.com/famousdrew/complimentary.git`
- [ ] Navigate: `cd complimentary/ml-training`
- [ ] Setup: `./setup.sh && source venv/bin/activate`
- [ ] Test: `python test_setup.py` (optional)
- [ ] Train: `python train_model.py`
- [ ] Convert: `python convert_to_coreml.py`
- [ ] Verify: `ls models/ComplimentScorer.mlpackage`

---

## 🎯 Next Session Goals

After training completes, we'll:

1. Open the iOS project in Xcode
2. Add the `.mlpackage` file
3. Create Swift bridge code
4. Connect to React Native
5. Test it live!

---

**Ready to start?** Head to your Mac and run the commands above! 🚀

---

## 📊 Current Todo List

- [x] Set up Python environment and install ML dependencies
- [x] Create training dataset of labeled compliments
- [ ] **← YOU ARE HERE →** Train the compliment scoring model
- [ ] Convert trained model to Core ML format
- [ ] Create Swift native module to bridge Core ML to React Native
- [ ] Integrate ML model into React Native app
- [ ] Test the ML integration end-to-end

---

Good luck! See you in the Mac session! 💪
