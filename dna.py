inputfile ="DNAFile.txt" # Store the string into the variable name inputfile
f = open(inputfile, "r") #open DNA.txt to read data in dna.py file
seq = f.read() # Read all of the contents of the file and store it in a variable called seq
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
    } #a dictionary that consist of keys and value is assigned to a varaible called Table
    # dictionaries are data structures are used to map arbitrary keys to value
     # prints out the value of the keys. Printed out the values as output using the keys
    name = input("Please enter your DNA sequence in CAPITAL letters:")
    print(table[name])#these key were given the value of x
    protein = ""
    if len(table) % 3 == 0: # if  3 can evenly go into the length of seq the return would be protein
        for i in range(0, len(table), 3): # the range function generated a list containing from 0, the number of items of that list up to 3
            codon = table[i:i + 3]
            protein += table[codon]
    return protein


def mutated(): #function to read from file

    #purpose of this function is to read data from the DNA file and create 2 new files to replace small "a"s with capital "A' and "T"

    f = open("DNAFile.txt", "r") # so here we have a variable that has data to open the DNAfile
    seq = f.read() # we then store data in variable to read the date

    locate_a = seq.find('a')  # create a variable that contains data to find all letter "a" within the file
    print(locate_a)

    mutation_file = open("mutatedDNA.txt","w") # a new variable created to store open a file and to use the write mode within it
    mutation_file.write(seq.replace("a","T")) # this line targets the file that is opened and replaces strings within it.
    mutation_file.close() # once the file has been opened and used, the file will then close

    normal_file = open("normalDNA.txt","w")
    normal_file.write(seq.replace("a", "A"))
    normal_file.close()

while True:
    translate(seq)
    mutated()
    break

#parameter comes at the declaration of the function ( consist of either a string or variable)
#argument is the value supplied to a parameter






