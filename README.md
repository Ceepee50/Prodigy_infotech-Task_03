# Prodigy_infotech-Task_03
# Password Strength Assessor

A simple Python tool to evaluate the strength of passwords and provide actionable feedback for improvement.

---

## Overview

The **Password Strength Assessor** is a lightweight Python script that checks the strength of a password based on the following criteria:

- **Length**: At least 8 characters.
- **Uppercase Letters**: Contains at least one uppercase letter.
- **Lowercase Letters**: Contains at least one lowercase letter.
- **Numbers**: Contains at least one digit.
- **Special Characters**: Contains at least one special character (e.g., `!`, `@`, `#`, etc.).

Based on these checks, the script assigns a strength rating of **Weak**, **Medium**, or **Strong** and provides feedback on how to improve the password.

---

## How It Works

The script uses a scoring system to evaluate the password:

1. **Length Check**: +1 point if the password is 8 characters or longer.
2. **Uppercase Check**: +1 point if the password contains at least one uppercase letter.
3. **Lowercase Check**: +1 point if the password contains at least one lowercase letter.
4. **Number Check**: +1 point if the password contains at least one digit.
5. **Special Character Check**: +1 point if the password contains at least one special character.

The total score determines the password's strength:
- **5 points**: Strong
- **3-4 points**: Medium
- **0-2 points**: Weak

---

## Usage

### Interactive Mode

Run the script directly to input a password and receive instant feedback:

```bash
python password_assessor.py
