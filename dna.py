inputfile ="DNAFile.txt" # Store the string into the variable name inputfile
f = open(inputfile, "r") #open DNA.txt to read data in dna.py file
seq = f.read() # Read all of the contents of the file and store it in a variable called
seq = seq.replace("\n", "") #replaces all newlines within the seq variable
seq = seq.replace("\r", "") #replaces all carriage return within the seq variable




def translate(seq): # created a new function that translate dna sequence into amino acids
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
    } #var table is assigned to a dictionary that consist of keys and value
    # dictionaries are data structures are used to map arbitrary keys to value
     # prints out the value of the keys. Printed out the values as out using the keys
    print(table['ATA'])
    print(table['CTC'])
    print(table['GTG'])
    print(table['TTC'])
    print(table['ATG'])
    print(table['TAA'] + table['TGA'] + table['TAG']) #these key were given the value of x
    protein = ""
    if len(seq) % 3 == 0: # if  3 can evenly go into the length of seq the return would be protein
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    return protein


def mutated(): #function to read from file

    locate_a = seq.find('a') # a var is assigned to the seq variable in order to find small letter "a"
    print(locate_a)


mutation_file = open("mutatedDNA.txt"w") # a variable is a assigned to the open function so that the file can be edited, 2 arguments are added which are the path and mode
mutation_file.write("mutated") # this line writes a string to the file, we use the write method to write to file
mutation_file.close() # once the file has been opened and used, the file will then close

nomal_file = open("normalDNA.txt","w")
nomal_file.write("normal")
nomal_file.close()

nomal_file= seq.replace('a', 'A') # we assigned a variable to DNA.textfile so that we can replace small letter a with UPPER case A in when the normalDNA.text file is opened
mutation_file =seq.replace('a', 'T') # we assigned a variable to DNA.textfile so that we can replace small letter a with UPPER case T when the mutatedDNA,text file is opened


while True:
    translate(seq)
    break






