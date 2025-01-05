import pandas as pd
import numpy as np
from collections import Counter

AMINO_ACIDS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X']
PADDING_VECTOR = [0] * 20 + [1]  # One-hot encoding for 'X'

def load_data(file_path):
    """Load the sequence data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        if 'Sequence' not in df.columns or 'ID' not in df.columns:
            raise ValueError("Input file must contain 'ID' and 'Sequence' columns.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except Exception as e:
        raise Exception(f"Error loading file: {e}")

def one_hot_encode(sequence, max_length):
    """One-hot encode a sequence with padding."""
    encoding = {aa: idx for idx, aa in enumerate(AMINO_ACIDS)}  # Create a mapping for quick lookup
    encoded_sequence = []
    for char in sequence:
        one_hot = [0] * 21
        if char in encoding:
            one_hot[encoding[char]] = 1
        encoded_sequence.extend(one_hot)
    
    # Pad the sequence to max_length
    padding_needed = max_length - len(sequence)
    encoded_sequence.extend(PADDING_VECTOR * padding_needed)
    return encoded_sequence

def calculate_composition(sequence):
    """Calculate letter composition as a frequency vector."""
    total_length = len(sequence)
    if total_length == 0:
        raise ValueError("Sequence length is zero.")
    
    # Use Counter for efficient counting
    counts = Counter(sequence)
    composition = [counts.get(aa, 0) / total_length for aa in AMINO_ACIDS]
    return composition

def process_sequences(df):
    """Process sequences to extract features."""
    try:
        max_length = df['Sequence'].str.len().max()
        df['OneHotEncoded'] = df['Sequence'].apply(lambda seq: one_hot_encode(seq, max_length))
        df['Composition'] = df['Sequence'].apply(calculate_composition)
        return df
    except Exception as e:
        raise Exception(f"Error processing sequences: {e}")

def main(file_path, num_rows=10):
    """Main function to process the data and display results."""
    try:
        df = load_data(file_path)
        print("Data loaded successfully.")

        processed_df = process_sequences(df)
        print("Sequences processed successfully.")

        # Filter the DataFrame to include only the specified number of rows
        filtered_df = processed_df.head(num_rows)

        # Print results in runtime
        for index, row in filtered_df.iterrows():
            print(f"ID: {row['ID']}")
            print(f"OneHotEncoded: {row['OneHotEncoded'][:10]}... (truncated for display)")
            print(f"Composition: {row['Composition']}\n")

        # below code is commented due to un-necessary feature
        # Save results to a CSV file
        # filtered_df[['ID', 'OneHotEncoded', 'Composition']].to_csv("runtime_processed_sequences.csv", index=False)
        # print(f"Processing complete. Results for {num_rows} rows saved to 'runtime_processed_sequences.csv'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main("uniprot_sequences.csv")
