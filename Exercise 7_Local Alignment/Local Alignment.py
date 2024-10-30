def initialize_matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]


def smith_waterman_lcs(seq1, seq2, match_score, mismatch_penalty, gap_penalty):
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = initialize_matrix(rows, cols)
    max_score = 0
    max_position = (0, 0)


    for i in range(1, rows):
        for j in range(1, cols):
            match = matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete = matrix[i - 1][j] + gap_penalty
            insert = matrix[i][j - 1] + gap_penalty
            matrix[i][j] = max(0, match, delete, insert)


            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_position = (i, j)


    i, j = max_position
    aligned_seq1 = []

    while i > 0 and j > 0 and matrix[i][j] != 0:
        if seq1[i - 1] == seq2[j - 1]:
            aligned_seq1.append(seq1[i - 1])
            i -= 1
            j -= 1
        else:
            break

    aligned_seq1.reverse()
    return ''.join(aligned_seq1), max_score



file_path1 = input("Enter the path to the first FASTA file including the file name and format: \n")
file_path2 = input("Enter the path to the second FASTA file including the file name and format: \n")
match_score = int(input("Enter the match score: "))
mismatch_penalty = int(input("Enter the mismatch penalty: "))
gap_penalty = int(input("Enter the gap penalty: "))

with open(file_path1, 'r') as file:
    seq1 = ''.join(line.strip() for line in file.readlines()[1:])

with open(file_path2, 'r') as file:
    seq2 = ''.join(line.strip() for line in file.readlines()[1:])

lcs, score = smith_waterman_lcs(seq1, seq2, match_score, mismatch_penalty, gap_penalty)


print(f"Result of local alignment: {lcs}")
print(f"Alignment score: {score}")
