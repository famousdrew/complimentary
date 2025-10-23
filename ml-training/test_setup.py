"""
Quick test to verify your setup is working correctly
Run this before training to catch any issues early
"""

import sys


def test_python_version():
    """Check Python version"""
    print("Testing Python version...")
    version = sys.version_info

    if version.major != 3:
        print("❌ Python 3 required")
        return False

    if version.minor < 9 or version.minor > 10:
        print(f"⚠️  Warning: Python {version.major}.{version.minor} detected")
        print("   Recommended: Python 3.9 or 3.10")
        print("   Python 3.11+ may have compatibility issues")
    else:
        print(f"✅ Python {version.major}.{version.minor} - Good!")

    return True


def test_imports():
    """Test if all required packages are installed"""
    print("\nTesting package imports...")

    packages = {
        'torch': 'PyTorch',
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'tqdm': 'tqdm',
    }

    all_good = True

    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} - not installed")
            all_good = False

    # Special check for coremltools (Mac only)
    try:
        import coremltools as ct
        print(f"✅ Core ML Tools (version {ct.__version__})")
    except ImportError:
        print("⚠️  Core ML Tools - not available (Mac required for conversion)")

    return all_good


def test_data():
    """Test if training data loads correctly"""
    print("\nTesting training data...")

    try:
        from training_data import get_training_data, get_data_stats

        data = get_training_data()
        stats = get_data_stats()

        print(f"✅ Loaded {stats['total_examples']} training examples")
        print(f"   Score distribution: {stats['score_distribution']}")

        return True
    except Exception as e:
        print(f"❌ Error loading training data: {e}")
        return False


def test_model():
    """Test if model architecture works"""
    print("\nTesting model architecture...")

    try:
        import torch
        from model import ComplimentScorer, Tokenizer

        # Create model
        model = ComplimentScorer(vocab_size=100, embedding_dim=32, hidden_dim=16)

        # Test forward pass
        dummy_input = torch.randint(0, 100, (1, 50))
        output = model(dummy_input)

        assert output.shape == (1, 5), "Output shape incorrect"

        print("✅ Model architecture works")

        # Test tokenizer
        tokenizer = Tokenizer(vocab_size=100)
        tokenizer.build_vocab(["hello world", "test example"])
        encoded = tokenizer.encode("hello test")

        print("✅ Tokenizer works")

        return True
    except Exception as e:
        print(f"❌ Error testing model: {e}")
        return False


def main():
    """Run all tests"""
    print("="*70)
    print("COMPLIMENTARY ML - SETUP TEST")
    print("="*70)
    print()

    results = []

    # Run tests
    results.append(("Python Version", test_python_version()))
    results.append(("Package Imports", test_imports()))
    results.append(("Training Data", test_data()))
    results.append(("Model Architecture", test_model()))

    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)

    all_passed = True
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {name}")
        if not passed:
            all_passed = False

    print("="*70)

    if all_passed:
        print("\n🎉 All tests passed! You're ready to train.")
        print("\nNext step: python train_model.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("1. Make sure virtual environment is activated")
        print("2. Run: pip install -r requirements.txt")
        print("3. Check Python version (should be 3.9 or 3.10)")

    print()


if __name__ == '__main__':
    main()
