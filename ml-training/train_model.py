"""
Training script for Compliment Scorer Model

This script:
1. Loads training data
2. Trains the LSTM model
3. Saves the trained PyTorch model
4. Converts it to Core ML format
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
from tqdm import tqdm
import os

from model import ComplimentScorer, Tokenizer
from training_data import get_training_data, get_data_stats


class ComplimentDataset(Dataset):
    """PyTorch Dataset for compliment data"""

    def __init__(self, data, tokenizer, max_length=100):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        text = item['text']
        # Score is 1-5, convert to 0-4 for classification
        label = item['score'] - 1

        # Encode text
        encoded = self.tokenizer.encode(text, self.max_length)

        return {
            'input': torch.tensor(encoded, dtype=torch.long),
            'label': torch.tensor(label, dtype=torch.long)
        }


def train_model(model, train_loader, criterion, optimizer, device, epochs=50):
    """
    Train the model

    Args:
        model: The neural network
        train_loader: DataLoader for training data
        criterion: Loss function
        optimizer: Optimizer
        device: CPU or CUDA
        epochs: Number of training epochs

    Returns:
        Trained model
    """
    model.to(device)
    model.train()

    print(f"\nTraining on {device}...")
    print(f"Epochs: {epochs}")
    print(f"Training samples: {len(train_loader.dataset)}\n")

    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        total = 0

        # Progress bar
        pbar = tqdm(train_loader, desc=f'Epoch {epoch+1}/{epochs}')

        for batch in pbar:
            inputs = batch['input'].to(device)
            labels = batch['label'].to(device)

            # Zero gradients
            optimizer.zero_grad()

            # Forward pass
            outputs = model(inputs)

            # Calculate loss
            loss = criterion(outputs, labels)

            # Backward pass
            loss.backward()

            # Update weights
            optimizer.step()

            # Statistics
            total_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            # Update progress bar
            pbar.set_postfix({
                'loss': f'{loss.item():.4f}',
                'acc': f'{100 * correct / total:.2f}%'
            })

        # Epoch summary
        avg_loss = total_loss / len(train_loader)
        accuracy = 100 * correct / total

        print(f'Epoch {epoch+1}: Loss = {avg_loss:.4f}, Accuracy = {accuracy:.2f}%')

    return model


def evaluate_model(model, tokenizer, device):
    """
    Test the model on example compliments

    Args:
        model: Trained model
        tokenizer: Tokenizer
        device: CPU or CUDA
    """
    model.eval()

    test_examples = [
        "Good job",
        "That was a nice presentation",
        "I noticed how you structured the data visualization to make trends obvious",
        "The way you explained that complex concept using analogies made it so much easier to understand",
        "When you took the time to mentor the new team member, showing patience and clear examples, it really helped them get up to speed faster and showed your leadership",
    ]

    print("\n" + "="*70)
    print("MODEL EVALUATION - Testing on example compliments")
    print("="*70)

    for text in test_examples:
        # Encode
        encoded = tokenizer.encode(text, max_length=100)
        input_tensor = torch.tensor([encoded], dtype=torch.long).to(device)

        # Predict
        with torch.no_grad():
            probs = model(input_tensor)
            predicted_class = torch.argmax(probs, dim=1)
            score = predicted_class.item() + 1
            confidence = probs[0][predicted_class].item()

        # Display
        stars = "⭐" * score + "☆" * (5 - score)
        print(f"\nCompliment: \"{text}\"")
        print(f"Score: {stars} ({score}/5)")
        print(f"Confidence: {confidence:.1%}")
        print(f"All probabilities: {probs[0].tolist()}")

    print("\n" + "="*70 + "\n")


def main():
    """Main training pipeline"""

    print("="*70)
    print("COMPLIMENTARY ML MODEL TRAINING")
    print("="*70)

    # Set random seed for reproducibility
    torch.manual_seed(42)
    np.random.seed(42)

    # Device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"\nUsing device: {device}")

    # Load training data
    print("\n📊 Loading training data...")
    data = get_training_data()
    stats = get_data_stats()

    print(f"Total examples: {stats['total_examples']}")
    print(f"Score distribution: {stats['score_distribution']}")

    # Build tokenizer
    print("\n🔤 Building vocabulary...")
    tokenizer = Tokenizer(vocab_size=5000)
    texts = [item['text'] for item in data]
    tokenizer.build_vocab(texts)

    # Create dataset and dataloader
    print("\n📦 Creating dataset...")
    dataset = ComplimentDataset(data, tokenizer, max_length=100)
    train_loader = DataLoader(dataset, batch_size=8, shuffle=True)

    # Create model
    print("\n🏗️  Creating model...")
    vocab_size = len(tokenizer.word2idx)
    model = ComplimentScorer(
        vocab_size=vocab_size,
        embedding_dim=128,
        hidden_dim=64,
        output_dim=5
    )

    # Count parameters
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Model parameters: {total_params:,}")
    print(f"Estimated size: ~{total_params * 4 / 1024 / 1024:.1f} MB")

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Train
    print("\n🚀 Starting training...")
    model = train_model(
        model,
        train_loader,
        criterion,
        optimizer,
        device,
        epochs=100  # More epochs since dataset is small
    )

    # Evaluate
    evaluate_model(model, tokenizer, device)

    # Save model
    print("💾 Saving model...")
    os.makedirs('models', exist_ok=True)

    # Save PyTorch model
    torch.save({
        'model_state_dict': model.state_dict(),
        'vocab_size': vocab_size,
        'word2idx': tokenizer.word2idx,
        'idx2word': tokenizer.idx2word,
    }, 'models/compliment_scorer.pth')

    print("✅ Model saved to models/compliment_scorer.pth")

    # Save tokenizer separately
    import pickle
    with open('models/tokenizer.pkl', 'wb') as f:
        pickle.dump(tokenizer, f)
    print("✅ Tokenizer saved to models/tokenizer.pkl")

    print("\n" + "="*70)
    print("TRAINING COMPLETE!")
    print("="*70)
    print("\nNext steps:")
    print("1. Run: python convert_to_coreml.py")
    print("2. This will create ComplimentScorer.mlpackage")
    print("3. Add the .mlpackage to your iOS project")
    print("="*70)


if __name__ == '__main__':
    main()
