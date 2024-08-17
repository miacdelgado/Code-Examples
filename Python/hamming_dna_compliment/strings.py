def get_hamming_distance(dna1, dna2): 
    dist = 0
    for i in range(0, len(dna1)):
        if dna1[i] != dna2[i]:
            dist += 1
    return dist

def get_dna_complement(dna):
    complement_dna = []
    for base in dna:
        if base == "A":
            complement_dna.append("T")
        elif base == "G":
            complement_dna.append("C")
        elif base == "T":
            complement_dna.append("A")
        elif base == "C":
            complement_dna.append("G")
    
    complement_dna_rev = complement_dna[::-1]
    complement_dna_final = "".join(complement_dna_rev)
    return complement_dna_final