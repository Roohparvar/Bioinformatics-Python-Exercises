def read_fasta(file_path):
    sequence = ""
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence


def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = "".join([complement[base] for base in reversed(dna_sequence)])
    return reverse_comp


file_path = input("Enter the path to the FASTA file including the file name and format: \n")
sequence = read_fasta(file_path)

print("---------------------------------------------------")
print("sequence:\n", sequence)
reverse_complement_sequence = reverse_complement(sequence)
print("---------------------------------------------------")
print("Reverse Complement:\n", reverse_complement_sequence)
print("---------------------------------------------------")