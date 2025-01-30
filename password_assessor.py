def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        strength += 1
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if any(not char.isalnum() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Determine password strength based on score
    if strength == 5:
        password_strength = "Strong"
    elif strength >= 3:
        password_strength = "Medium"
    else:
        password_strength = "Weak"
    
    return {
        "password_strength": password_strength,
        "feedback": feedback
    }

def main():
    password = input("Enter a password: ")
    assessment = assess_password_strength(password)
    print(f"Password Strength: {assessment['password_strength']}")
    if assessment['feedback']:
        print("Feedback:")
        for point in assessment['feedback']:
            print(point)

import unittest

class TestPasswordAssessor(unittest.TestCase):
    def test_weak_password(self):
        password = "abc"
        assessment = assess_password_strength(password)
        self.assertEqual(assessment["password_strength"], "Weak")

    def test_strong_password(self):
        password = "P@ssw0rd!"
        assessment = assess_password_strength(password)
        self.assertEqual(assessment["password_strength"], "Strong")

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:  # No command-line arguments
        main()
    else:
        unittest.main()