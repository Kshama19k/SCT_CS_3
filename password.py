import re

def assess_password_strength(password):
    score = 0
    reasons = []


    if len(password) >= 8:
        score += 1
    else:
        reasons.append(" Password should be at least 8 characters long.")

    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        reasons.append(" Add at least one uppercase letter (A-Z).")

   
    if re.search(r'[a-z]', password):
        score += 1
    else:
        reasons.append(" Add at least one lowercase letter (a-z).")

   
    if re.search(r'[0-9]', password):
        score += 1
    else:
        reasons.append(" Include at least one number (0-9).")

    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        reasons.append(" Include at least one special character (!@#$ etc).")

   
    strength_labels = {
        5: " Very Strong",
        4: " Strong",
        3: " Moderate",
        2: " Weak",
        1: " Very Weak",
        0: " Extremely Weak"
    }
    label = strength_labels.get(score, "Unknown")

    return score, label, reasons



if __name__ == "__main__":
    while True:
        password = input("\n Enter a password to assess: ")
        score, label, feedback = assess_password_strength(password)

        print(f"\nPassword Strength: {label} ({score}/5)")

        if feedback:
            print("Suggestions to improve:")
            for tip in feedback:
                print(" -", tip)

        again = input("\nWould you like to test another password? (y/n): ").strip().lower()
        if again != 'y':
            print(" Exiting password checker. Stay safe!")
            break
