#reference points
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Equal to or over 25 but below 30 they are slightly overweight
#Equal to or over 30 but below 35 they are obese
#Equal to or over 35 they are clinically obese

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
BMI = weight/height**2
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else :
    print(f"Your BMI is {BMI}, you are clinically obese.")



