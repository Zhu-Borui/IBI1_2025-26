data = { 'UK': [66.7, 69.2],
    'China': [1426, 1410],
    'Italy': [59.4, 58.9],
    'Brazil': [208.6, 212.0],
    'USA': [331.6, 340.1] }

growth_rates = {} # create an empty dictionary to store the growth rates
for country, pops in data.items(): # .items() returns a list of key-value pairs
    pop2020 = pops[0]
    pop2024 = pops[1]
    growth_rate = ((pop2024 - pop2020) / pop2020) * 100
    growth_rates[country] = growth_rate # store the growth rate in the dictionary

sorted_growth = sorted(growth_rates.items(),  # .items() returns a list of key-value pairs, sorted() sorts the list
                       key=lambda item: item[1], # sort by the second item in the tuple (the growth rate)
                       # lambda is an anonymous function that takes an item (a tuple) and returns the second element (the growth rate)
                       # item[1] is the growth rate, item[0] is the country name
                       reverse=True) 

print("Percentage changes (Descending):")
for country, change in sorted_growth:
    print(f"{country}: {change}%") # f-string is a way to format strings in Python, it allows you to embed expressions inside string literals using curly braces {}

# sorted_growth is a list of tuples (country, growth_rate) sorted by growth_rate in descending order
largest_increase = sorted_growth[0]
largest_decrease = sorted_growth[-1]

print(f"Largest increase: {largest_increase[0]} ({largest_increase[1]}%)")
print(f"Largest decrease: {largest_decrease[0]} ({largest_decrease[1]}%)")

import matplotlib.pyplot as plt

countries = [item[0] for item in sorted_growth]
changes = [item[1] for item in sorted_growth]

plt.figure(figsize=(10, 6))
plt.bar(countries, changes)

plt.axhline(0, color='black', linewidth=0.8) 
plt.ylabel('Percentage Change (%)')
plt.xlabel('Countries')
plt.title('Population Growth Rate (2020-2024)')
plt.show()

