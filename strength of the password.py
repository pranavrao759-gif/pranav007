
import re

def check_password_strength():
    """Checks the strength of a user-provided password based on several criteria."""
    
    # --- 1. Get Input ---
    # NOTE: In a real app, you'd use a special library to hide input.
    # For a command-line script, a standard input is fine.
    password = input("Enter your password to check: ")
    score = 0
    feedback = []

    # --- 2. Length Check (Score +1) ---
    if len(password) >= 8:
        score += 1
        feedback.append("✔️ Length is 8 or more characters.")
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # --- 3. Character Mix Checks (Score +1 for each type) ---
    # a) Uppercase Check
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✔️ Contains uppercase letters.")
    else:
        feedback.append("❌ Missing uppercase letters.")

    # b) Lowercase Check
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✔️ Contains lowercase letters.")
    else:
        feedback.append("❌ Missing lowercase letters.")

    # c) Number Check
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✔️ Contains numbers.")
    else:
        feedback.append("❌ Missing numbers (digits 0-9).")

    # d) Symbol Check
    # Searches for any non-alphanumeric character
    if re.search(r'[^a-zA-Z0-9\s]', password):
        score += 1
        feedback.append("✔️ Contains special symbols.")
    else:
        feedback.append("❌ Missing special symbols (like !@#$% etc.).")

    # --- 4. Repetition Check (Score -1 if found) ---
    # Looks for a character repeated three or more times consecutively
    if re.search(r'(.)\1\1', password):
        score -= 1
        feedback.append("⚠️ Weakness: Deducted 1 point for 3+ consecutive identical characters (e.g., 'aaa' or '111').")

    # --- 5. Final Output ---
    print("\n" + "="*40)
    print(f"Password Score: {score}/5")

    # Determine strength level
    if score >= 5:
        strength = "💪 VERY STRONG"
    elif score == 4:
        strength = "🟢 STRONG"
    elif score == 3:
        strength = "🟡 GOOD"
    else:
        strength = "🔴 WEAK"
    
    print(f"Strength Level: {strength}")
    print("="*40)
    
    # Print detailed feedback
    print("\nDetailed Feedback:")
    for item in feedback:
        print(f"- {item}")

# Run the function
check_password_strength()
