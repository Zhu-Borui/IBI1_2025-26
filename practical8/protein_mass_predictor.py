def predict_protein_mass(sequence):
    """
    Takes an amino acid sequence and returns the total mass in amu.
    Reports a ValueError if an invalid amino acid is found.
    """
    
    # Dictionary containing the residue masses from the provided table
    mass_table = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }

    total_mass = 0.0
    
    # Convert input to uppercase to prevent errors from lowercase letters
    sequence = sequence.upper()

    for aa in sequence:
        # Check if the amino acid is defined in our table
        if aa in mass_table:
            total_mass += mass_table[aa]
        else:
            # Report an error if it's not found
            raise ValueError(f"Error: Amino acid '{aa}' is invalid or has no recorded mass.")

    return total_mass

# Example usage

if __name__ == "__main__":
    
    # Example 1: A valid sequence
    valid_sequence = "SKADYEK"

    try:
        calculated_mass = predict_protein_mass(valid_sequence)
        # Formatting to 2 decimal places to match the input precision
        print(f"The predicted mass for {valid_sequence} is: {calculated_mass:.2f} amu")
    except ValueError as e:
        print(e)