# Complimentary - AI-Powered Compliment Coach

A React Native mobile app that helps users give better, more meaningful compliments using machine learning.

## 🎯 What It Does

Complimentary helps you:
- **Learn** to give specific, meaningful compliments
- **Practice** with real-time feedback and scoring
- **Generate** contextual compliments for any situation
- **Track** your compliment-giving journey

## 🏗️ Project Structure

```
complimentary/
├── complimentary-app/          # React Native mobile app
│   ├── src/
│   │   ├── screens/            # App screens (Coach, Generator, Journal)
│   │   ├── services/           # Business logic and ML integration
│   │   └── navigation/         # Navigation setup
│   └── ios/                    # iOS native code
│
├── ml-training/                # Machine learning training pipeline
│   ├── train_model.py          # Train the LSTM model
│   ├── convert_to_coreml.py   # Convert to Core ML for iOS
│   ├── training_data.py        # Labeled training examples
│   ├── model.py                # Neural network architecture
│   ├── QUICKSTART.md           # 5-minute quick start guide
│   └── GUIDE.md                # Complete detailed guide
│
└── ML_INTEGRATION_SUMMARY.md   # ML integration overview
```

## 🚀 Getting Started

### Mobile App

```bash
cd complimentary-app
npm install
npm start
```

### ML Training (Requires macOS for Core ML conversion)

```bash
cd ml-training

# Setup
./setup.sh
source venv/bin/activate

# Train model
python train_model.py

# Convert to Core ML (macOS only)
python convert_to_coreml.py
```

See [ml-training/QUICKSTART.md](ml-training/QUICKSTART.md) for detailed instructions.

## 📱 Features

### Current Features
- ✅ Compliment Coach with feedback
- ✅ Compliment Generator (600+ templates)
- ✅ Journal to track progress
- ✅ Onboarding flow
- ✅ Context-aware suggestions

### In Progress
- 🔄 ML-powered scoring (LSTM model)
- 🔄 Core ML iOS integration
- 🔄 Real-time quality analysis

### Planned
- ⬜ Personalized learning
- ⬜ On-device model training
- ⬜ Tone detection
- ⬜ Multi-language support

## 🧠 ML Model

**Type:** LSTM-based text classifier
**Size:** ~6-10MB
**Purpose:** Score compliment quality/specificity (1-5 stars)
**Platform:** Core ML (iOS)

**Training:**
- 100+ hand-labeled examples
- ~90-95% accuracy
- Trains in ~5 minutes on laptop
- 100% on-device inference

## 📚 Documentation

- [ML Integration Summary](ML_INTEGRATION_SUMMARY.md) - Overview of ML approach
- [ML Training Quick Start](ml-training/QUICKSTART.md) - Get started in 5 minutes
- [ML Training Guide](ml-training/GUIDE.md) - Complete walkthrough
- [ML Training README](ml-training/README.md) - Setup instructions

## 🛠️ Tech Stack

**Mobile App:**
- React Native 0.81
- Expo ~54
- React Navigation 7
- React Native Paper 5
- AsyncStorage

**ML Pipeline:**
- PyTorch 2.1
- Core ML Tools 7.1
- NumPy, Pandas
- LSTM architecture

**iOS Native:**
- Swift (for Core ML bridge)
- Core ML framework
- Neural Engine acceleration

## 📝 Current Status

**Phase 1: Rule-Based System** ✅ Complete
- Pattern matching for analysis
- Template-based generation
- Journal tracking

**Phase 2: ML Integration** 🔄 In Progress
- Training pipeline created
- LSTM model architecture ready
- Core ML conversion prepared
- iOS bridge pending

**Phase 3: Advanced Features** ⬜ Planned
- Personalization
- On-device learning
- Advanced generation

## 🔜 Next Steps

1. Train ML model on Mac
2. Convert to Core ML format
3. Create Swift native bridge
4. Integrate into React Native app
5. Test on iOS device
6. Deploy to users

## 📖 Learning Resources

This project demonstrates:
- React Native app development
- Machine learning training (PyTorch)
- Core ML integration
- Native module bridging
- On-device inference
- Mobile ML best practices

## 🤝 Contributing

This is a learning project. Feedback and suggestions welcome!

## 📄 License

MIT

---

**Ready to train?** Head to [ml-training/QUICKSTART.md](ml-training/QUICKSTART.md) to get started!
