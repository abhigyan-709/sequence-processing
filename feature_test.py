import pytest
import pandas as pd
from io import StringIO
from sequence_processing import load_data, one_hot_encode, calculate_composition, process_sequences

# Sample data for testing
TEST_CSV = """ID,Sequence
1,ACDEFGHIKLMNPQRSTVWY
2,ACDXFGHI
3,MNPQRSTVWY
"""

@pytest.fixture
def sample_dataframe():
    """Fixture to create a sample DataFrame."""
    data = StringIO(TEST_CSV)
    return pd.read_csv(data)

def test_load_data(sample_dataframe):
    """Test loading data from a CSV file."""
    # Write the sample data to a temporary file
    sample_csv = "test_sequences.csv"
    sample_dataframe.to_csv(sample_csv, index=False)
    
    # Test the function
    df = load_data(sample_csv)
    assert not df.empty, "DataFrame should not be empty"
    assert list(df.columns) == ["ID", "Sequence"], "Columns should match expected format"
    assert len(df) == 3, "DataFrame should have 3 rows"

def test_one_hot_encode():
    """Test one-hot encoding of a sequence."""
    sequence = "ACDX"
    max_length = 6
    encoded = one_hot_encode(sequence, max_length)
    assert len(encoded) == max_length * 21, "Encoded sequence length should match max_length * 21"
    assert encoded[:21] == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "First character encoding should match 'A'"
    assert encoded[-21:] == [0] * 20 + [1], "Padding should match 'X' encoding"

def test_calculate_composition():
    """Test calculating composition of a sequence."""
    sequence = "ACDX"
    composition = calculate_composition(sequence)
    assert len(composition) == 21, "Composition vector should have 21 elements"
    assert composition[0] == 0.25, "Frequency of 'A' should be 0.25"
    assert composition[20] == 0.25, "Frequency of 'X' should be 0.25"

def test_process_sequences(sample_dataframe):
    """Test processing sequences to extract features."""
    processed_df = process_sequences(sample_dataframe)
    assert "OneHotEncoded" in processed_df.columns, "'OneHotEncoded' column should exist in DataFrame"
    assert "Composition" in processed_df.columns, "'Composition' column should exist in DataFrame"
    assert len(processed_df) == 3, "Processed DataFrame should have the same number of rows as input"
    assert len(processed_df.loc[0, "OneHotEncoded"]) == 21 * len("ACDEFGHIKLMNPQRSTVWY"), "One-hot encoding length should match"

def test_main_workflow(monkeypatch, sample_dataframe):
    """Test the main workflow with user input."""
    from sequence_processing import main

    # Mock the input file and user input
    sample_csv = "test_sequences.csv"
    sample_dataframe.to_csv(sample_csv, index=False)
    monkeypatch.setattr('builtins.input', lambda _: "2")  # Simulate user input of '2'

    # Run the main function
    main(sample_csv)

    # Verify the output file
    output_csv = "processed_sequences.csv"
    df = pd.read_csv(output_csv)
    assert len(df) == 2, "Output CSV should contain 2 rows as per user input"
    assert list(df.columns) == ["ID", "OneHotEncoded", "Composition"], "Output columns should match expected format"
