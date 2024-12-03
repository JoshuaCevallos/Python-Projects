# List of weak passwords (these are common passwords hackers often try)
weak_passwords = [
    "123456", "password", "123456789", "12345678", "12345",
    "1234567", "qwerty", "abc123", "password1", "123123"
]

def check_password_strength(password):
    """
    Checks if a password is weak or strong.
    """
    if password in weak_passwords:
        return "Weak: This way too common c'mon think."
    elif len(password) < 8:
        return "Weak: Password is too short!"
    elif not any(char.isdigit() for char in password):
        return "Weak: Nope, needs at least one number"
    elif not any(char.isalpha() for char in password):
        return "Weak: At least one letter, c'mon!"
    else:
        return "Strong: Nice!"

# Main program
if __name__ == "__main__":
    print("We about to fix ya password problems")
    
    while True:
        # Ask the user for a password to check
        password = input("Let's see if it work...put it through: ").strip()  # Clean up extra spaces
        
        # Check the strength of the password
        result = check_password_strength(password)
        print(f"Password: '{password}' - {result}")
        
        # Break the loop if the password is strong
        if "Strong" in result:
            print("Alright cool, now this is a good password.")
            break
        else:
            print("Man, think of something better!")

