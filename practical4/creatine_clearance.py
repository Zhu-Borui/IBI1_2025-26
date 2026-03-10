# Pseudocode:
# 1. Store the person's data: age, weight, gender, and creatinine concentration (Cr).
# 2. Perform range checks for each variable:
#    - age should be < 100 years.
#    - weight should be > 20 kg and < 80 kg.
#    - Cr (creatinine) should be > 0 and < 100 micromol/l.
#    - gender must be either 'male' or 'female'.
# 3. If any value is out of range, print which variable needs correction.
# 4. If all values are valid:
#    a. Apply the Cockcroft-Gault Equation.
#    b. If the gender is female, multiply the result by 0.85.
#    c. Print the final CrCl value.

# input variables
age = 35
weight = 70
gender = "male"  # Options: "male" or "female"
creatinine = 80

# check the age
if age >= 100:
    print("The input variable age must be less than 100.")
# Check the weight range
elif weight <= 20 or weight >= 80:
    print("The input variable weight must be between 20 and 80.")
# Check the creatinine range    
elif creatinine <= 0 or creatinine >= 100:
    print("The input variable creatinine must be between 0 and 100")
# Check the gender
elif gender != "male" and gender != "female":
    print("The input variable gender must be either 'male' or 'female'.")
# If all checks are passed, calculate the crcl.
else: 
    crcl = ((140 - age) * weight) / (72 * creatinine)
    if gender == "female":
        crcl = crcl * 0.85
    # Display the final result using str() to combine text and numbers.
    print("The creatinine clearance is", str(crcl), "ml/min.")