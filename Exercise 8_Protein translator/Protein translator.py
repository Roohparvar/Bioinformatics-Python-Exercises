def translate_rna_to_protein(rna_sequence):
    protein_sequence = ""

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]

        if len(codon) == 3:
            amino_acid = codon_table.get(codon)
            if amino_acid == 'Stop':
                protein_sequence +=" (Stop Codon)\n"
            else:
                protein_sequence += amino_acid

    return protein_sequence


codon_table = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I',
    'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
    'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'AGU': 'S', 'AGC': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
    'CCG': 'P', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UAU': 'Y',
    'UAC': 'Y', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D',
    'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C',
    'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
    'GGG': 'G', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}


file_path = input("Enter the path to the FASTA file including the file name and format: \n")

rna_sequence = ""

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if not line.startswith('>'):
            rna_sequence += line


rna_sequence = rna_sequence.replace('T', 'U')
print("RNA sequence is:")
print(rna_sequence)


protein_sequence = translate_rna_to_protein(rna_sequence)
print("Protein sequence is:")
print(protein_sequence)