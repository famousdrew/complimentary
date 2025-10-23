"""
Convert trained PyTorch model to Core ML format

This script loads the trained model and converts it to .mlpackage
format for use in iOS apps.
"""

import torch
import coremltools as ct
import pickle
import os

from model import ComplimentScorer


def convert_to_coreml():
    """Convert the trained PyTorch model to Core ML format"""

    print("="*70)
    print("CONVERTING TO CORE ML")
    print("="*70)

    # Load the trained model
    print("\n📦 Loading trained model...")
    checkpoint = torch.load('models/compliment_scorer.pth', map_location='cpu')

    vocab_size = checkpoint['vocab_size']

    # Recreate model architecture
    model = ComplimentScorer(
        vocab_size=vocab_size,
        embedding_dim=128,
        hidden_dim=64,
        output_dim=5
    )

    # Load weights
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()

    print("✅ Model loaded successfully")

    # Load tokenizer
    print("\n🔤 Loading tokenizer...")
    with open('models/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)

    print(f"✅ Tokenizer loaded (vocab size: {len(tokenizer.word2idx)})")

    # Create example input for tracing
    print("\n🔍 Tracing model...")
    example_text = "This is a great compliment"
    example_encoded = tokenizer.encode(example_text, max_length=100)
    example_input = torch.tensor([example_encoded], dtype=torch.long)

    print(f"Example input shape: {example_input.shape}")

    # Trace the model
    traced_model = torch.jit.trace(model, example_input)

    print("✅ Model traced successfully")

    # Convert to Core ML
    print("\n🔄 Converting to Core ML...")

    # Define input
    input_shape = ct.Shape(shape=(1, 100))  # (batch_size, sequence_length)

    # Convert
    coreml_model = ct.convert(
        traced_model,
        inputs=[ct.TensorType(name="text", shape=input_shape, dtype=int)],
        outputs=[ct.TensorType(name="scores")],
        convert_to="mlprogram",  # Use ML Program (newer format)
        minimum_deployment_target=ct.target.iOS15,  # iOS 15+
    )

    print("✅ Conversion successful!")

    # Add metadata
    print("\n📝 Adding metadata...")

    coreml_model.author = "Complimentary App"
    coreml_model.license = "MIT"
    coreml_model.short_description = "Scores compliment quality and specificity on a 1-5 scale"
    coreml_model.version = "1.0.0"

    # Add input/output descriptions
    coreml_model.input_description["text"] = "Encoded text as array of word indices (length 100)"
    coreml_model.output_description["scores"] = "Probability distribution over 5 classes (1-5 stars)"

    # Save
    output_path = "models/ComplimentScorer.mlpackage"
    print(f"\n💾 Saving to {output_path}...")

    coreml_model.save(output_path)

    print("✅ Core ML model saved!")

    # Get file size
    import shutil
    size_mb = sum(
        os.path.getsize(os.path.join(dirpath, filename))
        for dirpath, _, filenames in os.walk(output_path)
        for filename in filenames
    ) / (1024 * 1024)

    print(f"\n📊 Model size: {size_mb:.2f} MB")

    # Test the Core ML model
    print("\n🧪 Testing Core ML model...")

    test_examples = [
        "Good job",
        "Your presentation was well organized and clear",
        "The way you explained that complex concept using analogies and real examples made it so much easier for everyone to understand",
    ]

    for text in test_examples:
        # Encode
        encoded = tokenizer.encode(text, max_length=100)
        input_dict = {"text": [encoded]}

        # Predict
        prediction = coreml_model.predict(input_dict)
        scores = prediction["scores"][0]

        # Get predicted class
        predicted_class = scores.argmax()
        predicted_score = predicted_class + 1
        confidence = scores[predicted_class]

        stars = "⭐" * predicted_score + "☆" * (5 - predicted_score)

        print(f"\nText: \"{text}\"")
        print(f"Score: {stars} ({predicted_score}/5)")
        print(f"Confidence: {confidence:.1%}")

    # Save vocabulary for iOS app
    print("\n📄 Saving vocabulary for iOS...")
    vocab_output = "models/vocabulary.txt"
    with open(vocab_output, 'w', encoding='utf-8') as f:
        for word, idx in sorted(tokenizer.word2idx.items(), key=lambda x: x[1]):
            f.write(f"{word}\t{idx}\n")

    print(f"✅ Vocabulary saved to {vocab_output}")

    print("\n" + "="*70)
    print("CONVERSION COMPLETE!")
    print("="*70)
    print(f"\n📦 Core ML model: {output_path}")
    print(f"📄 Vocabulary file: {vocab_output}")
    print(f"📊 Model size: {size_mb:.2f} MB")
    print("\n🎯 Next steps:")
    print("1. Copy ComplimentScorer.mlpackage to your iOS project")
    print("2. Copy vocabulary.txt to your iOS project resources")
    print("3. Create Swift bridge to use the model from React Native")
    print("="*70)


if __name__ == '__main__':
    if not os.path.exists('models/compliment_scorer.pth'):
        print("❌ Error: Trained model not found!")
        print("Please run: python train_model.py")
    else:
        convert_to_coreml()
