# Abcam AI Engineer

We would like to ask you to work a Python coding task and a 10min presentation in which you present your code and put it in the context of a pipeline.

## Coding Task 

### Introduction
This take-home coding task is designed to assess your coding and approach to software design.

As part of this task, you will (1) write some code to extract some features, and (2) produce a presentation on how you might incorporate this as part of a wider code stack.

Please note the following:

* Your code doesn’t necessarily need to run or be entirely complete; we are primarily looking for evidence of good software design principles and development practices, as well as scalability, extensibility etc. 
* Your code should be configured such that it can be readily packaged / installed. 
* You don’t have to spend too long on this, we’d suggest a maximum of 2 hours for both coding and preparing the PowerPoint. For example, you could explain what you would do in addition if you had more time. 
* We are looking for proficiency with commonly used Python data science libraries (pandas, numpy, scikit-learn, etc.), so please make use of these libraries where applicable even if implementable without them. 

### 1. Coding
#### The Brief
You are being given a CSV file containing sequence data extracted from UniProt named ‘uniprot_sequences.csv’. We are asking that you use Python to extract a series of features from the sequence data and present it in a performant data structure. You are allowed (and encouraged) to use the following Python libraries as well as anything from the Python standard library: pandas, numpy, and scikit-learn.
Please prepare code for this task along with a 10-minute presentation to review the code and discuss how it might be integrated into a larger code base. Details on the presentation are provided below.
 
#### Coding Task Details 
The provided csv file contains around 1,000 entries (or rows). Each row has a unique identifier and a sequence of letters. Note the sequence of letters is in fact an amino acid sequence, and each row corresponds to a protein, but this biological context is not relevant for this exercise – you can just think of the data as a couple of identifiers, each associated with a string of letters. 

The letters are drawn from the following list (with each letter corresponding to a different amino acid): 

``` 
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X'] 
```

When considering ordered features, such as one-hot encodings, use the above order. Note that the character ‘X’ indicates a missing or ambiguous amino acid in the sequence. 

Your task is to extract two features from each sequence and return a data structure that includes the listed features for all of the sequences given in ‘uniprot_sequences.csv’.

Expected features for each sequence: 
* *One Hot Encoded Letter Vector* - Each letter in the sequence is encoded as a 21-length one-hot encoded vector resulting in a vector of length L * 21, where L is the length of the longest sequence in the file. As an example, the amino acid ‘C’ (cysteine) can be encoded as the vector [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
Vectors of this feature should be the same length for all sequences, so for sequences shorter than the longest sequence in the set, pad the end of the sequence with the one-hot encoding of ‘X’ until it is of the same length as the longest.
* *Letter Composition* - The letter composition as a 21-length vector.
Your result should be a 21-length vector where each position describes the frequency of a letter in the sequence. Each position (based on the above array) would be the resulting value of An / A where An is the count of the letter in position n and A is the total number of letters in the sequence.  For example, the sequence ‘ADHAIPNNAP’ would result in an AAC vector of [0.3, 0, 0.1, 0, 0, 0, 0.1, 0.1, 0, 0, 0, 0.2, 0.2, 0, 0, 0, 0, 0, 0, 0, 0]. 

Your code must show evidence of good documentation following the Google Python style guide with docstrings and in-code comments where appropriate.
Please include a test suite using the testing library of your choice. 

### 2. Presentation
In addition to preparing the code, you should additionally prepare a presentation (slides, e.g. PowerPoint) around 10 minutes in length to discuss your coding design choices and outline how your code might be integrated into a larger code base comprising feature extraction and AI applications that use those features downstream. 

You may want to focus on the following topics:
-	How the code is designed or could be designed to ensure extensibility. 
-	How you envision the code being deployed. 
-	Where this code might sit within a wider code base of feature extraction and several AI models. 

## Summary

Your final deliverable will be the Python files containing your code and a prepared presentation. You do not need to include output of the program containing the features for the sequences, but there should be a single function call that will return the data structure containing all features for all sequences. 
