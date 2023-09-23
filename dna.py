def dna_strand(dna):
    dna = dna.replace('A', 't')
    dna = dna.replace('T', 'a')
    dna = dna.replace('C', 'g')
    dna = dna.replace('G', 'c')
    dna = dna.upper()  # Convert the entire string to uppercase
    return ('"' + dna_input + '"' + " --> " +  '"' + dna + '"')

dna_input = 'ATTGC'
print(dna_strand(dna_input))
