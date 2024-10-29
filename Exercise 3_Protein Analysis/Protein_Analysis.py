def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        current_seq = ""
        for line in file:
            if line.startswith(">"):
                if current_seq:
                    sequences[header] = current_seq
                header = line[1:].strip()
                current_seq = ""
            else:
                current_seq += line.strip()
        if current_seq:
            sequences[header] = current_seq
    return sequences


def analyze_protein_sequence(sequence):
    length = len(sequence)

    amino_acid_count = {}
    for amino_acid in sequence:
        if amino_acid in amino_acid_count:
            amino_acid_count[amino_acid] += 1
        else:
            amino_acid_count[amino_acid] = 1

    percentages = {aa: (count / length) * 100 for aa, count in amino_acid_count.items()}

    molecular_weight = calculate_molecular_weight(sequence)

    return {
        "length": length,
        "percentages": percentages,
        "molecular_weight": molecular_weight
    }


def calculate_molecular_weight(sequence):
    amino_acid_weights = {
        'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.15,
        'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.17,
        'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
        'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
    }

    total_weight = 0.0
    for amino_acid in sequence:
        total_weight += amino_acid_weights.get(amino_acid, 0)

    return total_weight


file_path = input("Enter the path to the FASTA file including the file name and format: \n")
sequences = read_fasta(file_path)


print("---------------------------------------------")
for header, sequence in sequences.items():
    analysis = analyze_protein_sequence(sequence)
    print(f"Analysis for {header}:")
    print(f"Sequence: {sequence}")
    print(f"Length: {analysis['length']} amino acids")
    print("Percentages of amino acids:")
    for aa, percentage in analysis['percentages'].items():
        print(f"{aa}: {percentage:.2f}%")
    print(f"Molecular Weight: {analysis['molecular_weight']:.2f} g/mol")
    print("---------------------------------------------")