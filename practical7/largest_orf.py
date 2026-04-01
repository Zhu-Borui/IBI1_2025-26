# define a function to find the largest open reading frame (ORF) in a given RNA sequence
def largest_ORF(rna_seq):
    start_codon = "AUG" 
    stop_codons = ["UAA", "UAG", "UGA"]
    largest_orf = "" # Initialize an empty string to store the largest ORF found
    max_length = 0 # Initialize a variable to keep track of the length of the largest ORF found
    for i in range(len(rna_seq) - 2):
        codon = rna_seq[i:i+3]
        if codon == start_codon:
                # Found a start codon, now look for the nearest stop codon
                # The gap between start and stop codon should be a multiple of 3
                for j in range(i + 3, len(rna_seq) - 2, 3):
                     stop_codon = rna_seq[j:j+3]
                     if stop_codon in stop_codons: # Check if the codon is a stop codon
                        orf = rna_seq[i:j+3] # Extract the ORF from start codon to stop codon
                        if len(orf) > len(largest_orf):
                            largest_orf = orf
                            max_length = len(largest_orf)
                        break  # Stop searching for this start codon after finding the first stop codon 
    return largest_orf, max_length

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

largest_orf, length = largest_ORF(seq)

if length > 0:
    print("Largest ORF:", largest_orf)
    print("Length:", length)
else:    
    print("No ORF found.")


# Method 2：
import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# (?=...): positive lookahead assertion, which allows us to find overlapping matches in the sequence.
# (?:...): non-capturing group, which groups the start codon and the stop codons together without creating a separate capturing group for them.
# *？: non-greedy match, which ensures that we find the shortest possible ORF between the start codon and the stop codon, rather than the longest possible ORF.
pattern = r'(?=(AUG(?:...)*?(?:UAA|UAG|UGA)))'

orfs = re.findall(pattern, seq)

if orfs:
    # Find the longest ORF from the list of ORFs found
    # key=len tells the max function to compare the ORFs based on their length, and return the one with the greatest length.
    longest_orf = max(orfs, key=len)
    # Print the longest ORF and its length
    print(f"largest orf: {longest_orf}")
    print(f"length: {len(longest_orf)} nucleotides")
else:
    print("No ORF found.")