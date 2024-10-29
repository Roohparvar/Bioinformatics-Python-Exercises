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


def analyze_rna_sequence(sequence):
    length = len(sequence)

    a_count = 0
    u_count = 0
    c_count = 0
    g_count = 0

    for nucleotide in sequence:
        if nucleotide == 'A':
            a_count += 1
        elif nucleotide == 'U':
            u_count += 1
        elif nucleotide == 'G':
            g_count += 1
        elif nucleotide == 'C':
            c_count += 1

    total_nucleotides = length
    a_percentage = (a_count / total_nucleotides) * 100
    u_percentage = (u_count / total_nucleotides) * 100
    g_percentage = (g_count / total_nucleotides) * 100
    c_percentage = (c_count / total_nucleotides) * 100

    gc_content = ((g_count + c_count) / total_nucleotides) * 100
    au_content = ((a_count + u_count) / total_nucleotides) * 100
    ag_content = ((a_count + g_count) / total_nucleotides) * 100
    gu_content = ((g_count + u_count) / total_nucleotides) * 100
    ac_content = ((a_count + c_count) / total_nucleotides) * 100
    uc_content = ((u_count + c_count) / total_nucleotides) * 100

    au_gc_ratio = (a_count + u_count) / (g_count + c_count) if (g_count + c_count) > 0 else None

    return {
        "length": length,
        "A%": a_percentage,
        "U%": u_percentage,
        "G%": g_percentage,
        "C%": c_percentage,
        "GC content": gc_content,
        "AU content": au_content,
        "AG content": ag_content,
        "GU content": gu_content,
        "AC content": ac_content,
        "UC content": uc_content,
        "AU/GC ratio": au_gc_ratio
    }


file_path = input("Enter the path to the FASTA file including the file name and format: \n")
sequences = read_fasta(file_path)

print("---------------------------------------------")
for header, sequence in sequences.items():
    analysis = analyze_rna_sequence(sequence)
    print(f"Analysis for {header}:")
    print(f"Sequence: {sequence}")
    for key, value in analysis.items():
        print(f"{key}: {value}")
    print("---------------------------------------------")
