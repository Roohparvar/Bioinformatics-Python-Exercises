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


def analyze_dna_sequence(sequence):
    length = len(sequence)

    a_count = 0
    t_count = 0
    c_count = 0
    g_count = 0

    for nucleotide in sequence:
        if nucleotide == 'A':
            a_count += 1
        elif nucleotide == 'T':
            t_count += 1
        elif nucleotide == 'G':
            g_count += 1
        elif nucleotide == 'C':
            c_count += 1

    total_nucleotides = length
    a_percentage = (a_count / total_nucleotides) * 100
    t_percentage = (t_count / total_nucleotides) * 100
    g_percentage = (g_count / total_nucleotides) * 100
    c_percentage = (c_count / total_nucleotides) * 100

    gc_content = ((g_count + c_count) / total_nucleotides) * 100
    at_content = ((a_count + t_count) / total_nucleotides) * 100
    ag_content = ((a_count + g_count) / total_nucleotides) * 100
    gt_content = ((g_count + t_count) / total_nucleotides) * 100
    ac_content = ((a_count + c_count) / total_nucleotides) * 100
    tc_content = ((t_count + c_count) / total_nucleotides) * 100

    at_gc_ratio = (a_count + t_count) / (g_count + c_count) if (g_count + c_count) > 0 else None

    return {
        "length": length,
        "A%": a_percentage,
        "T%": t_percentage,
        "G%": g_percentage,
        "C%": c_percentage,
        "GC content": gc_content,
        "AT content": at_content,
        "AG content": ag_content,
        "GT content": gt_content,
        "AC content": ac_content,
        "TC content": tc_content,
        "AT/GC ratio": at_gc_ratio
    }


file_path = input("Enter the path to the FASTA file including the file name and format: \n")
sequences = read_fasta(file_path)

print("---------------------------------------------")
for header, sequence in sequences.items():
    analysis = analyze_dna_sequence(sequence)
    print(f"Analysis for {header}:")
    print(f"Sequence: {sequence}")
    for key, value in analysis.items():
        print(f"{key}: {value}")
    print("---------------------------------------------")