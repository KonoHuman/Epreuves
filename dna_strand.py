def complementary_DNA(dna_strand):
    complementary = ""
    
    for char in dna_strand:
        if char == "A":
            complementary += "T"
        elif char == "T":
            complementary += "A"
        elif char == "C":
            complementary += "G"
        elif char == "G":
            complementary += "C"
    
    return complementary

input_dna = "ATTGC"
complementary_strand = complementary_DNA(input_dna)
print(complementary_strand)