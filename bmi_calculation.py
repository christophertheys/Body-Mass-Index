# BMI Calculator

# Program used to calculate a person's BMI
user_weight_in_kg = float(input("Please enter your weight in kilograms(kg)"))
user_height_in_m = float(input("Please enter your height in metres (m)"))

BMI = user_weight_in_kg/(user_height_in_m * user_height_in_m)
print("\n")

if BMI > 30.0:
    print(BMI)
    print("You're obese man... Your BMI is at {}".format(BMI))

elif BMI >= 25.0:
    print(BMI)
    print("You're overweight. Your BMI is at {}".format(BMI))

elif BMI >= 18.5:
    print(BMI)
    print("Normal BMI. Your BMI is at {}".format(BMI))

else:
    print(BMI)
    print("You are underweight... Your BMI is at {}".format(BMI))
