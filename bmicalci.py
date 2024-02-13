weight = float(input("Enter the weight in kilograms(kg): "))
height = float(input("Enter the height in centimeters(cm): "))

height_meters = height / 100
bmi = weight / (height_meters**2)
print(bmi)

if (bmi < 16):
    print ("Severely Underweight"), bmi

elif (bmi >= 16 and bmi < 18.5):   
    print ("Underweight"), bmi

elif (bmi >= 18.5 and bmi < 25):
    print ("Healthy"), bmi

elif (bmi >= 25 and bmi < 30):
   print ("Overweight"), bmi

elif (bmi >=30):
    print ("Obese"), bmi