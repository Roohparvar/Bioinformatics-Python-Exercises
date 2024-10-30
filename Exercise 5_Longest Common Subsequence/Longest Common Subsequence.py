def longest_common_subsequence(sequence1, sequence2):
    m, n = len(sequence1), len(sequence2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]

    lcs = []
    while m > 0 and n > 0:
        if sequence1[m - 1] == sequence2[n - 1]:
            lcs.append(sequence1[m - 1])
            m -= 1
            n -= 1
        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        else:
            n -= 1

    lcs.reverse()
    return ''.join(lcs)


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


lcs_result = longest_common_subsequence(sequence1, sequence2)
print(f"\nLongest Common Subsequence (LCS): {lcs_result}")
