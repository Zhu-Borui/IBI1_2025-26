heart_rates	=[72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# calculates the total number of heart rates, the average heart rate.
print("The total number of heart rates is:", len(heart_rates), 
      "The average heart rate is:", sum(heart_rates)/len(heart_rates))

# counts the number of heart rates that are low (<60), normal (60-100), and high (>100).
L = 0
N = 0
H = 0
for i in heart_rates:
    if i < 60:
        L = L + 1
    elif i > 120:
        H = H + 1
    else:
        N = N + 1
print("The number of low heart rates is:", L,
      "The number of normal heart rates is:", N,
        "The number of high heart rates is:", H)

categories = {'Low': L, 'Normal': N, 'High': H}

print("The category with the largest number of patients is:", 
      max(categories, key=categories.get)) 
# The max function is used to find the key with the largest value in the categories dictionary.
# The key argument is used to specify a function that takes a key as input and returns a value that is used for sorting.

import matplotlib.pyplot as plt

labels = ['Low (<60)', 'Normal (60-120)', 'High (>120)']
sizes = [L, N, H]
colors = ['#ff9999', '#66b3ff', '#99ff99']

plt.figure(figsize=(8, 6))

plt.title('Distribution of Heart Rate Categories')

# create a pie chart. 
# The sizes argument specifies the size of each slice. 
# The labels argument specifies the labels for each slice.
# The colors argument specifies the colors for each slice.
plt.pie(sizes, labels=labels, colors=colors) 
plt.show()





