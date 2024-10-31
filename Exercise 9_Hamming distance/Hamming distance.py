def read_fasta(file_path):
    sequence = ""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                sequence += line
    return sequence


def calculate_hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        print("Error: Sequences must have the same length for Hamming distance calculation.")
        return None
    distance = sum(1 for a, b in zip(seq1, seq2) if a != b)

    alignment_line = ''.join('|' if a == b else ' ' for a, b in zip(seq1, seq2))

    print("Sequence 1: ", seq1)
    print("            ", alignment_line)
    print("Sequence 2: ", seq2)

    return distance


file1_path = input("Enter the path to the first FASTA file including the file name and format: \n")
file2_path = input("Enter the path to the second FASTA file including the file name and format: \n")


sequence1 = read_fasta(file1_path)
sequence2 = read_fasta(file2_path)


if len(sequence1) == len(sequence2):
    hamming_distance = calculate_hamming_distance(sequence1, sequence2)
    print("The Hamming distance between the sequences is:", hamming_distance)
else:
    print("The sequences have different lengths. Please provide sequences with the same length.")