# -------------------------------
# Example 1: Student Grade Evaluation
# -------------------------------
marks = 92

if marks >= 90:   # if marks are 90 or above
    print("Excellent! Grade A")
elif marks >= 75: # if marks are between 75 and 89
    print("Very Good! Grade B")
elif marks >= 60: # if marks are between 60 and 74
    print("Good! Grade C")
elif marks >= 40: # if marks are between 40 and 59
    print("Pass! Grade D")
else:             # if marks are below 40
    print("Fail! Better luck next time")

# -------------------------------
# Example 2: Age Group Classification
# -------------------------------
age = 25

if age < 13:      # less than 13 years
    print("Child")
elif age < 20:    # between 13 and 19
    print("Teenager")
elif age < 35:    # between 20 and 34
    print("Young Adult")
elif age < 60:    # between 35 and 59
    print("Adult")
else:             # 60 and above
    print("Senior Citizen")

# -------------------------------
# Example 3: Shopping Discount System
# -------------------------------
amount = 1200

if amount >= 2000:   # if purchase is 2000 or more
    print("You get 30% discount")
elif amount >= 1000: # if purchase is between 1000 and 1999
    print("You get 20% discount")
elif amount >= 500:  # if purchase is between 500 and 999
    print("You get 10% discount")
else:                # if purchase is below 500
    print("No discount available")

# -------------------------------
# Example 4: Weather Suggestion
# -------------------------------
temperature = 15

if temperature > 30:   # hot weather
    print("It's hot! Wear light clothes.")
elif temperature > 20: # pleasant weather
    print("Nice weather! Perfect for outing.")
elif temperature > 10: # cool weather
    print("Cool weather! Wear a jacket.")
else:                  # very cold
    print("Too cold! Stay warm inside.")