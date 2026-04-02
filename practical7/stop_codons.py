input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stop_codons = {'TAA', 'TAG', 'TGA'}

# Open the input FASTA file for reading and the output file for writing
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Split the entire file by ">" to process block by block
    # [1:] skips the first empty string created by the split
    entries = f_in.read().split(">")[1:]
    
    for entry in entries:
        # Each entry corresponds to one gene and its sequence. 
        # The first line is the header, and the rest are the sequence lines.
        # splitlines(): splits the entry into lines.
        lines = entry.strip().splitlines()
        # The first line is the header, and the rest are the sequence lines.
        # We will join the sequence lines into a single string for easier processing.
        header = lines[0]
        # Join the multi-line sequence into a single continuous string without empty spaces or newlines.
        sequence = "".join(lines[1:])
        
        # Extract the sequence name
        # Based on the assignment example, it is the first word after ">" (e.g., YBR024W_mRNA)
        gene_name = header.split()[0]
        
        # Find the position of the first 'ATG' to establish the Open Reading Frame (ORF)
        start_idx = sequence.find("ATG")
        
        # If 'ATG' is found, we will look for in-frame stop codons starting from that position.
        # != -1 means that 'ATG' was found in the sequence.
        if start_idx != -1:
            found_stops = set() 
            
            # Iterate starting from ATG, step by 3 bases to stay in-frame
            for i in range(start_idx, len(sequence) - 2, 3):
                codon = sequence[i:i+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break  # Stop after finding the first in-frame stop codon, as per the assignment instructions

            # If at least one in-frame stop codon is found, write to the new file
            if found_stops:
                # Use a semicolon ";" to separate the gene name and stop codons
                # sorted() is used to ensure the stop codons are listed in a consistent order (TAA, TAG, TGA)
                stops_str = ";".join(sorted(found_stops))
                # Write the header line in the format: >gene_name;stop_codons
                f_out.write(f">{gene_name};{stops_str}\n")
                
                # Write the sequence, formatting it to standard FASTA (60 characters per line)
                for i in range(0, len(sequence), 60):
                    f_out.write(sequence[i:i+60] + "\n")

print("Processing complete. Check stop_genes.fa")