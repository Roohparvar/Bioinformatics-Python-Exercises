def print_alignment_with_matches(alignment_seq1, alignment_seq2):
    matches = ''.join('|' if alignment_seq1[i] == alignment_seq2[i] else ' ' for i in range(len(alignment_seq1)))

    print("\nAlignment Result:")
    print(f"First sequence:  {alignment_seq1}")
    print(f"                 {matches}")
    print(f"Second sequence: {alignment_seq2}\n")


def initialize_matrix(rows, cols, gap_penalty):
    matrix = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        matrix[i][0] = i * gap_penalty
    for j in range(cols):
        matrix[0][j] = j * gap_penalty
    return matrix


def global_alignment(seq1, seq2, match_score, mismatch_penalty, gap_penalty):
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = initialize_matrix(rows, cols, gap_penalty)

    for i in range(1, rows):
        for j in range(1, cols):
            match = matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete = matrix[i - 1][j] + gap_penalty
            insert = matrix[i][j - 1] + gap_penalty
            matrix[i][j] = max(match, delete, insert)

    aligned_seq1, aligned_seq2 = '', ''
    i, j = len(seq1), len(seq2)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap_penalty:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    return aligned_seq1, aligned_seq2, matrix[len(seq1)][len(seq2)]


file_path1 = input("Enter the path to the first FASTA file including the file name and format: \n")
file_path2 = input("Enter the path to the second FASTA file including the file name and format: \n")
match_score = int(input("Enter the match score: "))
mismatch_penalty = int(input("Enter the mismatch penalty: "))
gap_penalty = int(input("Enter the gap penalty: "))

with open(file_path1, 'r') as file:
    seq1 = ''.join(line.strip() for line in file.readlines()[1:])

with open(file_path2, 'r') as file:
    seq2 = ''.join(line.strip() for line in file.readlines()[1:])

aligned_seq1, aligned_seq2, score = global_alignment(seq1, seq2, match_score, mismatch_penalty, gap_penalty)


print_alignment_with_matches(alignment_seq1=aligned_seq1, alignment_seq2=aligned_seq2)
print(f"Alignment score: {score}")