import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\zhuxl\\Desktop\\IBI-semester2\\IBI1_2025-26\\IBI1_2025-26\\practical10")

# Load the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

###############################################################################

dalys_data.head(5)
dalys_data.info()
dalys_data.describe()
dalys_data.iloc[0,3]
dalys_data.iloc[2,0:5]
dalys_data.iloc[0:2,:]
dalys_data.iloc[0:10:2,0:5] # Take once every other line
dalys_data.iloc[0:3,[0,1,3]]

my_columns = [True, True, False, True] # False: skip this column
dalys_data.iloc[0:3,my_columns]
# If the length of my_cilumns is not equal to the number of columns, there will be an error

dalys_data.loc[2:4,"Year"] # 4 is included
dalys_data.loc[dalys_data["Year"] > 2010]
dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]

recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]



###############################################################################

# Showing the third and fourth columns (Year and DALYs) for the first 10 rows
afghanistan_first_10 = dalys_data.iloc[0:10, 2:4]
print("--- Afghanistan's Year and DALYs (First 10 rows) ---")
print(afghanistan_first_10)

# The year that reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan is 1998.

# Use a Boolean to show all years for which DALYs were recorded in Zimbabwe
is_zimbabwe = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[is_zimbabwe, "Year"]
print("\n--- Years recorded in Zimbabwe ---")
print(zimbabwe_years.to_string(index=False)) # don't show the index column

# The first year for which these data were recorded in Zimbabwe is 1990, and the last year is 2019.

# Retrieve values to find max and min DALYs in 2019
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_idx = recent_data["DALYs"].idxmax() # Index position of the maximum value
min_idx = recent_data["DALYs"].idxmin()

country_max = recent_data.loc[max_idx, "Entity"]
country_min = recent_data.loc[min_idx, "Entity"]

print(f"\nCountry with Maximum DALYs in 2019: {country_max}")
print(f"Country with Minimum DALYs in 2019: {country_min}")

# COMMENT: In 2019, the country with the maximum DALYs was Lesotho, and the country with the minimum DALYs was Singapore.

# Plot showing the DALYS over time in Singapore (Minimum in 2019)
singapore_data = dalys_data.loc[dalys_data["Entity"] == "Singapore"]

plt.figure(figsize=(8, 5))
plt.plot(singapore_data["Year"], singapore_data["DALYs"], 'bo-', label="Singapore")
plt.title("DALYs Over Time in Singapore")
plt.xlabel("Year")
# plt.xticks(singapore_data["Year"], rotation=-90)
plt.ylabel("DALYs")
plt.legend()
plt.grid(True)
plt.show()

#  Question: How has the relationship between the DALYs in China and the UK changed over time?
china_data = dalys_data.loc[dalys_data["Entity"] == "China"]
uk_data = dalys_data.loc[dalys_data["Entity"] == "United Kingdom"]

plt.figure(figsize=(8, 5))
plt.plot(china_data["Year"], china_data["DALYs"], 'r-', label="China") # r-: Red solid line
plt.plot(uk_data["Year"], uk_data["DALYs"], 'g--', label="United Kingdom")
plt.title("DALYs Comparison Over Time: China vs United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.legend()
plt.grid(True)
plt.show()