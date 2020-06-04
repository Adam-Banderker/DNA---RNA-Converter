inputfile ="DNA.txt" # Store the string into the variable name inputfile
f = open(inputfile, "r") #open DNA.txt to read data in dna.py file
seq = f.read() # Read all of the contents of the file and store it in a variable called
seq = seq.replace("\n", "") #replaces all newlines within the seq variable
seq = seq.replace("\r", "") #replaces all carriage return within the seq variable




def translate(seq):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': 'X', 'TAG': 'X',
        'TGC': 'C', 'TGT': 'C', 'TGA': 'X', 'TGG': 'W',
    }
    print(table['ATT'] + table['CTC'] + table['GTG'] + table['TTC'] + table['ATG'])
    print(table['TAA'] + table['TGA'] + table['TAG'])
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    return protein
translate(seq)

def mutated():
    locate_a = seq.find('a')
    print(locate)


mutation_DNA = open("mutatedDNA","w")
mutation_DNA.write("mutated")
mutation_DNA.close()

normal_DNA = open("normalDNA","w")
normal_DNA.write("normal")
normal_DNA.close()

normal_DNA= seq.replace('a', 'A')
mutation_DNA =seq.replace('a', 'T')

while True:
    translate(seq)
    break






