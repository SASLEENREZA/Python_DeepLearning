codon = input("enter the codon sequence:")

print([codon[i:i+3] for i in range(0, len(codon), 3)])
