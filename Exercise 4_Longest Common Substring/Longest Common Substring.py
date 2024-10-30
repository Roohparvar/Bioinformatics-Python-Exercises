def longest_common_substring(sequence1, sequence2):
    m, n = len(sequence1), len(sequence2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    if max_length == 0:
        return None

    return sequence1[end_index - max_length + 1: end_index + 1]


def print_sequence(sequence, name):
    print(f"{name} sequence: {sequence}")


file_path1 = input("Enter the path to the first FASTA file including the file name and format: \n")
file_path2 = input("Enter the path to the second FASTA file including the file name and format: \n")


with open(file_path1, 'r') as file:
    sequence1 = ''.join(line.strip() for line in file.readlines()[1:])

with open(file_path2, 'r') as file:
    sequence2 = ''.join(line.strip() for line in file.readlines()[1:])


print_sequence(sequence1, "Sequence1")
print_sequence(sequence2, "Sequence2")


lcs_result = longest_common_substring(sequence1, sequence2)
print("\nLongest Common Substring:")
print(lcs_result)