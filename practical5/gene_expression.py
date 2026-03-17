# import necessary libraries
import matplotlib.pyplot as plt

# Create a dictionary to store gene expression levels
genes = {'TP53': 12.4, 'ECFR': 15.1, 
         'BRCR1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
print("Initial gene expression levels:", genes)

# Add a new gene expression level to the dictionary
genes['MYC'] = 11.6

# Extract gene symbols and expression levels for plotting
gene_symbols = list(genes.keys())
expression_levels = list(genes.values())

# Plot the gene expression levels using a bar chart
plt.figure(figsize=(10, 6)) # Set the figure size 
plt.bar(gene_symbols, expression_levels, color='skyblue')
plt.xlabel('Gene Symbols') # Label for x-axis
plt.ylabel('Expression Levels') 
plt.title('Gene Expression Levels') # Title of the plot
plt.xticks(rotation=45) # Rotate x-axis labels for 45 degrees
plt.show()

# Access the expression level of a specific gene

# pseudocode:
# 1. Define a variable 'gene_input' with the name of the gene you want
# 2. Check if 'gene_input' is in the 'genes' dictionary
# 3. If it is, print the expression level of that gene
# 4. If it is not, print a message saying the gene is not found in the dictionary

gene_input = 'TP53'
if gene_input in genes:
    print("The expression level of", gene_input, "is", genes[gene_input])
else: 
    print("Gene", gene_input, "is not found in the dictionary.")

# Calculate the average expression level across all genes
average_expression = sum(expression_levels) / len(expression_levels)
print("The average expression level across all genes is:", average_expression)