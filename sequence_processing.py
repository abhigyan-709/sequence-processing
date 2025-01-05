import pandas as pd


# Constants
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
    try:
        encoded_sequence = []
        for char in sequence:
            one_hot = [1 if char == aa else 0 for aa in AMINO_ACIDS]
            encoded_sequence.extend(one_hot)
        # Pad the sequence to max_length
        padding_needed = max_length - len(sequence)
        encoded_sequence.extend(PADDING_VECTOR * padding_needed)
        return encoded_sequence
    except Exception as e:
        raise ValueError(f"Error in one-hot encoding sequence '{sequence}': {e}")

def calculate_composition(sequence):
    """Calculate letter composition as a frequency vector."""
    try:
        total_length = len(sequence)
        if total_length == 0:
            raise ValueError("Sequence length is zero.")
        composition = [sequence.count(aa) / total_length for aa in AMINO_ACIDS]
        return composition
    except Exception as e:
        raise ValueError(f"Error calculating composition for sequence '{sequence}': {e}")

def process_sequences(df):
    """Process sequences to extract features."""
    try:
        max_length = df['Sequence'].str.len().max()
        df['OneHotEncoded'] = df['Sequence'].apply(lambda seq: one_hot_encode(seq, max_length))
        df['Composition'] = df['Sequence'].apply(calculate_composition)
        return df
    except Exception as e:
        raise Exception(f"Error processing sequences: {e}")


def main(file_path):
    """Main function to process the data and display results."""
    try:
        # Load data
        df = load_data(file_path)
        print("Data loaded successfully.")

        # Process sequences
        processed_df = process_sequences(df)
        print("Sequences processed successfully.")

        # Ask the user how many rows to display and save
        while True:
            try:
                num_rows = int(input("Enter the number of rows to display and save (e.g., 10 or 20 or any number): "))
                if num_rows <= 0 or num_rows > len(processed_df):
                    print(f"Please enter a number between 1 and {len(processed_df)}.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Filter the DataFrame to include only the specified number of rows
        filtered_df = processed_df.head(num_rows)

        # Print results in runtime
        for index, row in filtered_df.iterrows():
            print(f"ID: {row['ID']}")
            print(f"OneHotEncoded: {row['OneHotEncoded'][:10]}... (truncated for display)")
            print(f"Composition: {row['Composition']}\n")

        # Save results to a CSV file
        filtered_df[['ID', 'OneHotEncoded', 'Composition']].to_csv("processed_sequences.csv", index=False)
        print(f"Processing complete. Results for {num_rows} rows saved to 'processed_sequences.csv'.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main("uniprot_sequences.csv")
