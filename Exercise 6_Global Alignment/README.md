# Global Alignment of Sequences

This script performs a Global Alignment between two sequences using the Needleman-Wunsch algorithm. The alignment maximizes the score based on user-provided values for match, mismatch, and gap penalties.

## Features

- **Input**: Reads two sequences from FASTA format files.
- **Custom Scoring**: Allows the user to input custom scores for match, mismatch, and gap penalties.
- **Global Alignment**: Performs global alignment of the two sequences.
- **Output**: Prints the aligned sequences, with gaps ("-") inserted as needed for alignment.
- **Match Indication**: Matches are indicated by the symbol `|`, while mismatches and gaps are left as spaces.
- **Final Alignment Score**: Prints the final alignment score for the alignment achieved.

This script is particularly useful in bioinformatics for comparing sequences, analyzing evolutionary relationships, and studying the functional similarities of proteins or nucleic acids.
