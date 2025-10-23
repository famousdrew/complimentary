"""
Compliment Scorer Model Architecture

A lightweight LSTM-based text classifier optimized for mobile deployment.
"""

import torch
import torch.nn as nn


class ComplimentScorer(nn.Module):
    """
    LSTM-based model for scoring compliment quality/specificity.

    Architecture:
    1. Embedding layer (converts words to vectors)
    2. LSTM layer (processes sequence)
    3. Fully connected layers (classification)
    4. Output: score (1-5) and confidence

    Model size: ~5-10MB
    """

    def __init__(self, vocab_size=5000, embedding_dim=128, hidden_dim=64, output_dim=5):
        super(ComplimentScorer, self).__init__()

        # Embedding layer: converts word indices to dense vectors
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)

        # LSTM layer: processes the sequence of word embeddings
        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_dim,
            num_layers=1,
            batch_first=True,
            bidirectional=False
        )

        # Dropout for regularization
        self.dropout = nn.Dropout(0.3)

        # Fully connected layers
        self.fc1 = nn.Linear(hidden_dim, 32)
        self.fc2 = nn.Linear(32, output_dim)

        # Activation functions
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        """
        Forward pass

        Args:
            x: Input tensor of word indices, shape (batch_size, sequence_length)

        Returns:
            scores: Probability distribution over 5 classes (1-5 stars)
        """
        # Embedding: (batch, seq_len) -> (batch, seq_len, embedding_dim)
        embedded = self.embedding(x)

        # LSTM: (batch, seq_len, embedding_dim) -> (batch, seq_len, hidden_dim)
        lstm_out, (hidden, cell) = self.lstm(embedded)

        # Take the last hidden state
        # hidden shape: (1, batch, hidden_dim) -> (batch, hidden_dim)
        last_hidden = hidden.squeeze(0)

        # Dropout
        dropped = self.dropout(last_hidden)

        # Fully connected layers
        fc1_out = self.relu(self.fc1(dropped))
        fc2_out = self.fc2(fc1_out)

        # Softmax to get probabilities
        scores = self.softmax(fc2_out)

        return scores

    def predict_score(self, x):
        """
        Predict star rating and confidence

        Args:
            x: Input tensor of word indices

        Returns:
            score: Predicted star rating (1-5)
            confidence: Confidence of prediction (0-1)
        """
        with torch.no_grad():
            probs = self.forward(x)

            # Get the predicted class (0-4) and add 1 to make it 1-5
            predicted_class = torch.argmax(probs, dim=1)
            score = predicted_class + 1

            # Confidence is the max probability
            confidence = torch.max(probs, dim=1)[0]

            return score.item(), confidence.item()


class Tokenizer:
    """
    Simple tokenizer for converting text to indices
    """

    def __init__(self, vocab_size=5000):
        self.vocab_size = vocab_size
        self.word2idx = {'<PAD>': 0, '<UNK>': 1}
        self.idx2word = {0: '<PAD>', 1: '<UNK>'}
        self.word_counts = {}

    def build_vocab(self, texts):
        """Build vocabulary from training texts"""
        # Count word frequencies
        for text in texts:
            words = text.lower().split()
            for word in words:
                self.word_counts[word] = self.word_counts.get(word, 0) + 1

        # Sort by frequency and take top vocab_size - 2 (excluding PAD and UNK)
        sorted_words = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        top_words = sorted_words[:self.vocab_size - 2]

        # Build word2idx and idx2word
        for idx, (word, count) in enumerate(top_words, start=2):
            self.word2idx[word] = idx
            self.idx2word[idx] = word

        print(f"Vocabulary built with {len(self.word2idx)} words")

    def encode(self, text, max_length=100):
        """
        Convert text to indices

        Args:
            text: Input text string
            max_length: Maximum sequence length

        Returns:
            List of word indices
        """
        words = text.lower().split()
        indices = []

        for word in words[:max_length]:
            idx = self.word2idx.get(word, self.word2idx['<UNK>'])
            indices.append(idx)

        # Pad to max_length
        while len(indices) < max_length:
            indices.append(self.word2idx['<PAD>'])

        return indices

    def decode(self, indices):
        """Convert indices back to text"""
        words = []
        for idx in indices:
            if idx == self.word2idx['<PAD>']:
                break
            word = self.idx2word.get(idx, '<UNK>')
            words.append(word)
        return ' '.join(words)


if __name__ == '__main__':
    # Test the model
    print("Testing ComplimentScorer model...")

    # Create model
    model = ComplimentScorer(vocab_size=5000, embedding_dim=128, hidden_dim=64)

    # Create dummy input (batch_size=2, seq_len=100)
    dummy_input = torch.randint(0, 5000, (2, 100))

    # Forward pass
    output = model(dummy_input)
    print(f"Output shape: {output.shape}")  # Should be (2, 5)
    print(f"Output (probabilities): {output}")

    # Predict score
    score, confidence = model.predict_score(dummy_input[0:1])
    print(f"\nPredicted score: {score} stars")
    print(f"Confidence: {confidence:.2%}")

    # Test tokenizer
    print("\n\nTesting Tokenizer...")
    tokenizer = Tokenizer(vocab_size=100)

    sample_texts = [
        "This is a great compliment",
        "You did an amazing job",
        "The way you handled that was impressive"
    ]

    tokenizer.build_vocab(sample_texts)

    text = "This is a test"
    encoded = tokenizer.encode(text, max_length=20)
    decoded = tokenizer.decode(encoded)

    print(f"Original: {text}")
    print(f"Encoded: {encoded[:10]}...")
    print(f"Decoded: {decoded}")

    print("\n✅ Model architecture test complete!")
