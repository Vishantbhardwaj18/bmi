def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m) * height (m))
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")

    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    classification = classify_bmi(bmi)

    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {classification}")

if __name__ == "__main__":
    main()
