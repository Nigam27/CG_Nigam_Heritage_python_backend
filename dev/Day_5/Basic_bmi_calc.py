# Basic BMI Calculator
name = input("Enter your name : ")
weight = float(input("Weight in kg : "))
height = float(input("Height in meters : "))
bmi = weight / (height ** 2)
if bmi < 18.5:
 category = "Underweight"
 advice = "Eat more nutritious food and gain healthy weight."
elif bmi < 25:
 category = "Normal Weight"
 advice = "Great! Maintain your current lifestyle."
elif bmi < 30:
 category = "Overweight"
 advice = "Consider regular exercise and balanced diet."
else:
 category = "Obese"
 advice = "Consult a doctor for a personalised health plan."
print(f"\n--- BMI Report for {name} ---")
print(f"BMI Score : {bmi:.2f}")
print(f"Category : {category}")
print(f"Advice : {advice}")
