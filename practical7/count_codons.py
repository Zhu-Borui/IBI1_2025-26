import sys
from collections import Counter
import matplotlib.pyplot as plt

# This script reads a FASTA file, 
# identifies the longest ORF for each gene that ends with a specified stop codon, 
# counts the codons in those ORFs, 
# and generates a pie chart of the codon distribution
def read_fasta(filename):
    # """^^^""" means "docstring" - a string that describes what the function does. 
    # It's a good practice to include docstrings in your functions to explain their purpose and usage.
    """Reads a FASTA file and returns {seq_id: sequence}"""
    sequences = {}
    # Initiate curr_id to None to handle cases where the file might not start with a header line.
    curr_id = None
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('>'):
                    curr_id = line[1:].strip()
                    sequences[curr_id] = ""
                # If we encounter a line that doesn't start with '>' and we have a current ID, 
                # we append the line to the sequence for that ID.
                elif curr_id:
                    sequences[curr_id] += line.upper() #.upper() ensures that all sequences are in uppercase
    # Handle the case where the file might be empty or not properly formatted (no headers).
    except FileNotFoundError: 
        print(f"Error: File '{filename}' not found.")
        # If the file is not found, we print an error message and exit the program with a non-zero status to indicate an error.
        # 1 is a common convention for indicating that the program exited due to an error.
        sys.exit(1) 
    return sequences

# The find_longest_orf_codons function scans through the given DNA sequence to find all ORFs that start with 'ATG' and end with the specified target stop codon.
def find_longest_orf_codons(sequence, target_stop):
    """
    Find the longest ORF ending exactly with the target_stop codon.
    Returns the list of codons *upstream* of that stop (including ATG).
    """
    stop_codons = {'TAA', 'TAG', 'TGA'}
    max_length = -1 # Initialize max_length to -1 to ensure that any valid ORF found will be considered longer than this initial value.
    best_codons = []

    for i in range(len(sequence) - 2):          
        if sequence[i:i+3] == 'ATG':
            current_codons = ['ATG'] 
            
            for j in range(i + 3, len(sequence) - 2, 3):   
                codon = sequence[j:j+3]
                
                if len(codon) != 3:
                    break

                if codon in stop_codons:
                    if codon == target_stop:
                        if len(current_codons) > max_length:
                            max_length = len(current_codons)
                            # If we find a longer ORF, we update best_codons to be a copy of current_codons.
                            # [:] creates a shallow copy of the list, which is important to avoid modifying best_codons when we later modify current_codons.
                            best_codons = current_codons[:]
                    break
                else:
                    # If the codon is not a stop codon, we add it to the current_codons list and continue scanning.
                    current_codons.append(codon)

    return best_codons

# The main function orchestrates the overall workflow of the script, 
# including user input, reading the FASTA file, finding ORFs, counting codons, and generating the pie chart.
def main():
    # User input
    valid_stops = {'TAA', 'TAG', 'TGA'}
    user_stop = input("Please input a stop codon (TAA, TAG, TGA): ").strip().upper()
    
    if user_stop not in valid_stops:
        print("Invalid input. Stop codon must be TAA, TAG, or TGA.")
        sys.exit(1)

    # Read FASTA
    fasta_file = 'stop_genes.fa'          
    print(f"Reading sequences from {fasta_file}...")
    genes = read_fasta(fasta_file)

    # Find longest ORF codons and count them
    total_codon_counts = Counter()
    valid_gene_count = 0

    print(f"Scanning for longest ORFs ending with {user_stop}...")
    for gene_id, seq in genes.items():
        
        seq = ''.join(seq.split())
        
        # If the sequence is shorter than 6 nucleotides, it cannot contain a valid ORF
        if len(seq) < 6: 
            continue

        orf_codons = find_longest_orf_codons(seq, user_stop)
        
        # If orf_codons is not empty, it means we found a valid ORF for this gene.
        if orf_codons:
            # We update the total_codon_counts with the codons from this ORF. 
            total_codon_counts.update(orf_codons)
            valid_gene_count += 1

    if valid_gene_count == 0:
        print(f"No valid ORFs ending with {user_stop} were found.")
        sys.exit(0) # 0 indicates successful completion, even if no valid ORFs were found.

    print(f"Found valid ORFs in {valid_gene_count} gene(s). Generating pie chart...")

    # Create and save pie chart
    # We extract the labels (codons) and their corresponding counts from total_codon_counts to create the pie chart.
    labels = list(total_codon_counts.keys())
    sizes = list(total_codon_counts.values())

    # We set the figure size to be larger
    plt.figure(figsize=(14, 10))
    # autopct='%1.1f%%' adds percentage labels to each slice of the pie chart, showing the percentage of the total for each codon.
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
            # textprops={'fontsize': 8} sets the font size of the labels and percentage text to 8
            textprops={'fontsize': 8}, pctdistance=0.85)
    
    # plt.axis('equal') ensures that the pie chart is drawn as a circle rather than an ellipse
    plt.axis('equal')
    
    plt.title(f'In-frame Codon Distribution for ORFs Ending in {user_stop}\n'
              f'({valid_gene_count} genes, longest ORF selected per gene)',
              fontsize=15, pad=25)

    output_filename = f'codon_distribution_{user_stop}.png'
    plt.savefig(output_filename, bbox_inches='tight', dpi=300)
    print(f"Success! Pie chart saved as '{output_filename}'")

# The following line checks if the script is being run directly (as the main program) rather than imported as a module in another script.
if __name__ == "__main__":
    main()